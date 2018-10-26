import subprocess
from pyat.config import *


class ADB(object):
    def __init__(self, device_id=None):
        adb_exec = ["adb", ]
        if device_id:
            adb_exec += ["-s", device_id]
        self.adb_exec = adb_exec

    def run(self, command):
        final_command = [*self.adb_exec, *command]
        return lambda: self._exec(final_command)

    @staticmethod
    def _exec(command):
        adb_process = subprocess.Popen(command, stdout=subprocess.PIPE)
        exec_result, exec_err = adb_process.communicate(timeout=DEFAULT_TIMEOUT)
        if exec_err:
            raise RuntimeError(exec_err.decode())
        logger.info(TAG_EXEC_CMD, cmd=command, result=exec_result)
        return exec_result.decode()
