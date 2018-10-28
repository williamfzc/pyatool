from pyatool.adb import ADB
from pyatool import binder
from pyatool.config import *

import importlib


class PYAToolkit(object):
    def __init__(self, device_id, need_log=None):
        self.device_id = device_id
        self.adb = ADB(device_id)

        self._need_log = bool(need_log)

    @classmethod
    def bind_cmd(cls, func_name, command):
        return binder.add(func_name, command)

    @classmethod
    def bind_func(cls, real_func):
        return binder.add(real_func.__name__, real_func)

    @classmethod
    def current_function(cls):
        return binder.get_all()

    def __getattr__(self, item):
        if not binder.is_existed(item):
            raise AttributeError('function {} not found'.format(item))
        command = binder.get(item)

        # is real function
        if callable(command):
            return lambda *args, **kwargs: command(*args, toolkit=self, **kwargs)
        # is command
        return lambda: self.adb.run(command)


# build-in functions bind here
extra_functions = importlib.import_module('pyatool.extras')
for each_func in extra_functions.__all__:
    function_obj = getattr(extra_functions, each_func)
    PYAToolkit.bind_func(real_func=function_obj)
logger.info(TAG_BINDER, msg='standard package loaded')
