import requests
import tempfile
import os
import platform


SYSTEM_TYPE = platform.system()


def hello_world(toolkit=None):
    # toolkit contains some tools for development
    # get device id
    device_id = toolkit.device_id
    print(device_id)
    # use adb
    toolkit.adb.run(['shell', 'ps'])


def install_from(url=None, path=None, toolkit=None):
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
    filter_name = 'findstr' if SYSTEM_TYPE == 'Windows' else 'grep'
    return toolkit.adb.run(['shell', 'dumpsys',  'activity', 'top', '|', filter_name, 'ACTIVITY'])


def show_package(toolkit=None):
    return toolkit.adb.run(['shell', 'pm', 'list', 'package'])


__all__ = [
    'hello_world',

    'install_from',
    'show_package',
    'get_current_activity',
]
