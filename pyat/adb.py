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
        return self._exec(final_command)

    @staticmethod
    def _exec(command):
        adb_process = subprocess.Popen(command, stdout=subprocess.PIPE)
        exec_result, exec_err = adb_process.communicate(timeout=DEFAULT_TIMEOUT)
        if adb_process.returncode != 0:
            feedback = 'unknown error happened when execute {}, view terminal for detail'.format(command)
            if exec_err:
                feedback = exec_err.decode()
            raise RuntimeError(feedback)
        logger.info(TAG_EXEC_CMD, cmd=command, result=exec_result)
        return exec_result.decode()
