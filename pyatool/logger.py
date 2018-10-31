import structlog
import logging


logger = structlog.getLogger(__name__)

info = logger.info
warn = logger.warn
error = logger.error


# need log?
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
