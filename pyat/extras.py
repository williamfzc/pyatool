import requests
import tempfile
import os


def download_and_install(url, toolkit=None):
    resp = requests.get(url)
    if not resp.ok:
        return False
    with tempfile.NamedTemporaryFile('wb+', suffix='.apk', delete=False) as temp:
        temp.write(resp.content)
        temp.close()
        toolkit.adb.run(['install', '-r', temp.name])
        os.remove(temp.name)
    return True


__all__ = [
    'download_and_install',
]
