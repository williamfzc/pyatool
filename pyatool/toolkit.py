from pyatool.adb import ADB
from pyatool import binder
import pyatool.config as conf
import pyatool.logger as logger
import importlib


class PYAToolkit(object):
    def __new__(cls, *args, **kwargs):
        # load standard functions
        cls._bind_standard()
        return super(PYAToolkit, cls).__new__(cls)

    def __init__(self, device_id, mode=None):
        self.device_id = device_id

        if mode == 'remote':
            self.adb = ADB(device_id, mode)
        else:
            self.adb = ADB(device_id, 'local')

    @classmethod
    def bind_cmd(cls, func_name, command):
        command = command.split(' ')
        return binder.add(func_name, lambda toolkit: toolkit.adb.run(command))

    @classmethod
    def bind_func(cls, real_func):
        return binder.add(real_func.__name__, real_func)

    @classmethod
    def _bind_standard(cls):
        # build-in functions bind here
        logger.info(conf.TAG_BINDER, msg=' standard package loading ... '.center(40, '-'))
        extra_functions = importlib.import_module('pyatool.extras')
        for each_func in extra_functions.__all__:
            function_obj = getattr(extra_functions, each_func)
            PYAToolkit.bind_func(real_func=function_obj)
        logger.info(conf.TAG_BINDER, msg=' standard package loaded '.center(40, '-'))

    def __getattr__(self, item):
        if not binder.is_existed(item):
            raise AttributeError('function {} not found'.format(item))
        command = binder.get(item)
        return lambda *args, **kwargs: command(*args, toolkit=self, **kwargs)

    @classmethod
    def current_function(cls):
        return binder.get_all()

    @classmethod
    def change_conf(cls, name, value):
        if hasattr(conf, name):
            setattr(conf, name, value)
            return True
        return False

    @classmethod
    def switch_logger(cls, status):
        return logger.switch(status)
