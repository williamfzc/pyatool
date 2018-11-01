import requests
import tempfile
import os
import platform

SYSTEM_TYPE = platform.system()


def hello_world(toolkit=None):
    """
    test only

    :param toolkit:
    :return:
    """
    # toolkit contains some tools for development
    # get device id
    device_id = toolkit.device_id
    print(device_id)
    # use adb
    toolkit.adb.run(['shell', 'ps'])


def install_from(url=None, path=None, toolkit=None):
    """
    根据url或path安装apk

    :param url:
    :param path:
    :param toolkit:
    :return:
    """
    if (not (url or path)) or (url and path):
        raise TypeError('need url or path for installation, not both or none')
    if url and not path:
        return _install_from_url(url, toolkit)
    else:
        return _install_from_path(path, toolkit)


def _install_from_url(url, toolkit=None):
    resp = requests.get(url)
    if not resp.ok:
        return False
    with tempfile.NamedTemporaryFile('wb+', suffix='.apk', delete=False) as temp:
        temp.write(resp.content)
        temp.close()
        toolkit.adb.run(['install', '-r', '-d', '-t', temp.name])
        os.remove(temp.name)
    return True


def _install_from_path(path, toolkit=None):
    return toolkit.adb.run(['install', '-r', '-d', '-t', path])


def get_current_activity(toolkit=None):
    """
    获取设备的当前activity名称

    :param toolkit:
    :return:
    """

    # TODO if sh has installed in windows, command is same as linux ..
    # filter_name = 'findstr' if SYSTEM_TYPE == 'Windows' else 'grep'
    return toolkit.adb.run(['shell', 'dumpsys', 'activity', 'top', '|', 'grep', 'ACTIVITY'])


def is_installed(package_name, toolkit=None):
    """
    检测包是否已被安装到设备上

    :param package_name:
    :param toolkit:
    :return:
    """
    return package_name in show_package(toolkit)


def show_package(toolkit=None):
    """
    展示设备上所有已安装的包

    :param toolkit:
    :return:
    """
    return toolkit.adb.run(['shell', 'pm', 'list', 'package'])


def clean_cache(package_name, toolkit=None):
    """
    清理对应包的缓存

    :param package_name:
    :param toolkit:
    :return:
    """
    return toolkit.adb.run(['shell', 'pm', 'clear', package_name])


def uninstall(package_name, toolkit=None, save_data=None):
    """
    卸载指定包

    :param package_name:
    :param toolkit:
    :param save_data:
    :return:
    """
    if save_data:
        cmd_list = ['uninstall', '-k', package_name]
    else:
        cmd_list = ['uninstall', package_name]
    return toolkit.adb.run(cmd_list)


__all__ = [
    'hello_world',

    'install_from',
    'show_package',
    'get_current_activity',
    'is_installed',
    'clean_cache',
    'uninstall',
]
