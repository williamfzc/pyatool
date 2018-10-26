from pyat.adb import ADB
from pyat import binder


class PYAToolkit(object):
    def __init__(self, device_id, need_log=None):
        self._device_id = device_id
        self._need_log = bool(need_log)
        self._adb = ADB(device_id)

    @classmethod
    def bind_cmd(cls, func_name, command):
        return binder.add(func_name, command)

    @classmethod
    def bind_func(cls, real_func):
        return binder.add(real_func.__name__, real_func)

    def __getattr__(self, item):
        if not binder.is_existed(item):
            raise AttributeError('function {} not found'.format(item))
        command = binder.get(item)

        # is real function
        if callable(command):
            return lambda: command(device_id=self._device_id)
        # is command
        return self._adb.run(command)

    def is_available(self):
        self._adb
