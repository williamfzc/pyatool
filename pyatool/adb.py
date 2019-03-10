import subprocess
import re
from pyatool.logger import logger
import pyatool.config as conf


class ADB(object):
    def __init__(self, device_id, mode=None):
        self.adb_exec = [conf.ADB_EXECUTOR, '-s', device_id]
        self.device_id = device_id
        self.device_ip = None

        # remote connect
        if mode and mode == 'remote':
            self.device_ip = self._enable_remote_connect()
            self.adb_exec = [conf.ADB_EXECUTOR, '-s', self.device_ip]

        # show current configure
        logger.debug('adb executor ready: <{}>'.format(self.adb_exec))

    def run(self, command):
        final_command = [*self.adb_exec, *command]
        return self._exec(final_command)

    @staticmethod
    def _exec(command):
        """ throw RuntimeError when command failed """
        adb_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exec_result, exec_err = adb_process.communicate(timeout=conf.DEFAULT_TIMEOUT)
        if adb_process.returncode != 0:
            if exec_err:
                feedback = exec_err.decode()
            else:
                feedback = 'unknown error happened when execute {}, view terminal for detail'.format(command)
            raise RuntimeError(feedback)
        logger.debug('execute: <{}> => result: <{}>'.format(command, exec_result))
        return exec_result.decode()

    @staticmethod
    def restart_adb():
        """ restart adb server """
        subprocess.check_call(['adb', 'kill-server'])
        subprocess.check_call(['adb', 'start-server'])

    def _get_ip_address(self):
        result = self.run(['shell', 'ifconfig', 'wlan0'])
        return re.findall(r'inet\s*addr:(.*?)\s', result, re.DOTALL)[0]

    def _enable_remote_connect(self):
        """ enable remote connect, and return device's ip address """
        ip_address = self._get_ip_address()
        self.run(['tcpip', '5555'])
        self._exec([conf.ADB_EXECUTOR, 'connect', ip_address])
        return ip_address
