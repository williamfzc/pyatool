from pyat.config import *


# TODO need a standard output? like json
_func_map = dict()


def is_existed(func_name):
    return func_name in _func_map


def add(func_name, command):
    if not is_existed(func_name):
        if callable(command):
            _func_map[func_name] = command
        else:
            _func_map[func_name] = command.split(' ')
        logger.info(TAG_BINDER, msg='function {} added'.format(func_name))
        return True
    logger.warn(TAG_BINDER, msg='function already existed', name=func_name)
    return False


def remove(func_name):
    if func_name in _func_map:
        del _func_map[func_name]
        logger.info(TAG_BINDER, msg='function {} removed'.format(func_name))
        return True
    logger.warn(TAG_BINDER, msg='function {} not existed'.format(func_name))
    return False


def get(func_name):
    return _func_map.get(func_name)


def get_all():
    return _func_map
