import requests
import tempfile
import os


def hello_world(toolkit=None):
    # toolkit contains some tools for development
    # get device id
    device_id = toolkit.device_id
    print(device_id)
    # use adb
    toolkit.adb.run(['shell', 'ps'])


def download_and_install(url, toolkit=None):
    resp = requests.get(url)
    if not resp.ok:
        return False
    with tempfile.NamedTemporaryFile('wb+', suffix='.apk', delete=False) as temp:
        temp.write(resp.content)
        temp.close()
        toolkit.adb.run(['install', '-r', '-d', '-t', temp.name])
        os.remove(temp.name)
    return True


def show_package(toolkit):
    return toolkit.adb.run(['shell', 'pm', 'list', 'package'])


__all__ = [
    'hello_world',

    'download_and_install',
    'show_package',
]
