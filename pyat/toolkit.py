from pyat.adb import ADB
from pyat import binder


class PYAToolkit(object):
    def __init__(self, device_id, need_log=None):
        self.device_id = device_id
        self._need_log = bool(need_log)
        self._adb = ADB(device_id)

    @classmethod
    def bind(cls, func_name, command):
        return binder.add(func_name, command)

    def __getattr__(self, item):
        if not binder.is_existed(item):
            raise AttributeError('function {} not found'.format(item))
        command = binder.get(item)
        return self._adb.run(command)
