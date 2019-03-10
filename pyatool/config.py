"""
global configure
"""
import platform

# config
# default adb command timeout
DEFAULT_TIMEOUT = 30

# system
# 'Linux', 'Windows' or 'Darwin'.
SYSTEM_NAME = platform.system()
NEED_SHELL = SYSTEM_NAME != 'Windows'
ADB_EXECUTOR = 'adb'
