import structlog
import logging


logger = structlog.getLogger(__name__)

info = logger.info
warn = logger.warn
error = logger.error


# need log?
def switch(status):
    global info, warn, error
    status = bool(status)
    if status:
        info = logger.info
        warn = logger.warn
        error = logger.error
        return status
    empty_func = lambda *_, **__: None
    info, warn, error = empty_func, empty_func, empty_func
    return status


# TODO: still didn't work, related to https://github.com/hynek/structlog/issues/30
def set_log_level(level):
    level_dict = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'warn': logging.WARN,
        'error': logging.ERROR,
    }
    if level not in level_dict:
        return NameError('level {} not supported'.format(level))
    logger.setLevel(level_dict[level])


# default to no log
switch(False)
