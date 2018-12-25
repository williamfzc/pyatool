"""
global configure
"""
import platform
import subprocess


# TAG
TAG_EXEC_CMD = 'EXEC_CMD'
TAG_BINDER = 'BINDER'
TAG_DEVICE = 'DEVICE'

# config
# default adb command timeout
DEFAULT_TIMEOUT = 30

# system
# 'Linux', 'Windows' or 'Darwin'.
SYSTEM_NAME = platform.system()
NEED_SHELL = SYSTEM_NAME != 'Windows'
if SYSTEM_NAME == 'Windows':
    ADB_EXECUTOR = subprocess.getoutput('where adb')
else:
    ADB_EXECUTOR = subprocess.getoutput('which adb')
