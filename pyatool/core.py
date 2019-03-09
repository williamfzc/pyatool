from pyatool.adb import ADB
from pyatool import binder
import pyatool.config as conf
from pyatool.logger import logger
import pyatool.extras as extras


class PYAToolkit(object):
    _instance_dict = dict()

    def __new__(cls, *args, **kwargs):
        # load standard functions
        # for looking up
        cls.standard_func = extras
        # alias
        cls.std = cls.standard_func

        return super(PYAToolkit, cls).__new__(cls)

    def __init__(self, device_id, mode=None):
        """
        init toolkit

        :param device_id:
        :param mode: 'local' or 'remote'

        remote mode:
        1. get ip address
        2. enable device's port 5555
        3. adb connect {ip_address}
        4. change base adb command to: `adb -s {ip_address}`

        communication between device and PC will use wireless way.
        and when you execute `adb devices`, it would become two devices:
        device id and device ip (but actually they are one)
        """
        # init
        self.device_id = device_id
        if mode == 'remote':
            self.adb = ADB(device_id, mode)
        else:
            self.adb = ADB(device_id, 'local')
        self.device_ip = self.adb.device_ip

        # storage
        self._instance_dict[device_id] = self

    @classmethod
    def bind_cmd(cls, func_name, command):
        command = command.split(' ')
        return binder.add(func_name, lambda toolkit: toolkit.adb.run(command))

    @classmethod
    def bind_func(cls, real_func):
        return binder.add(real_func.__name__, real_func)

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
        name = 'pyatool'
        if status:
            logger.enable(name)
            return
        logger.disable(name)

    def terminate(self):
        """ destroy instance """
        if self.device_id in self._instance_dict:
            del self._instance_dict[self.device_id]

    def __getattr__(self, item):
        # is standard function?
        if hasattr(self.standard_func, item):
            command = getattr(self.standard_func, item)
            return lambda *args, **kwargs: command(*args, toolkit=self, **kwargs)
        # is custom function?
        if not binder.is_existed(item):
            raise AttributeError('function {} not found'.format(item))
        command = binder.get(item)
        return lambda *args, **kwargs: command(*args, toolkit=self, **kwargs)
