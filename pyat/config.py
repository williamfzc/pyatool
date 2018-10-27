import structlog


logger = structlog.getLogger()

# TAG
TAG_EXEC_CMD = 'EXEC_CMD'
TAG_BINDER = 'BINDER'

# config
# default adb command timeout
DEFAULT_TIMEOUT = 15


__all__ = [
    'logger',

    'TAG_EXEC_CMD',
    'TAG_BINDER',

    'DEFAULT_TIMEOUT',
]
