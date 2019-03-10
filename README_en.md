# pyatool

[中文README](https://github.com/williamfzc/pyatool/blob/master/README.md)

[![Maintainability](https://api.codeclimate.com/v1/badges/5f6647a3121aa7d278ab/maintainability)](https://codeclimate.com/github/williamfzc/pyatool/maintainability)
[![PyPI version](https://badge.fury.io/py/pyatool.svg)](https://badge.fury.io/py/pyatool)
[![Downloads](https://pepy.tech/badge/pyatool)](https://pepy.tech/project/pyatool)
[![Documentation Status](https://readthedocs.org/projects/pyatool/badge/?version=latest)](https://pyatool.readthedocs.io/en/latest/?badge=latest)

> python android toolkit 🔨

## TL;DR

Directly call standard API.

```python
from pyatool import PYAToolkit

# init
device = PYAToolkit('123456F')

# 1. call it directly
package_list = device.show_package()
# 2. or, call it via std
package_list = device.std.show_package(toolkit=device)

# return content depends on called function
print(package_list)
```

View all API we provided [here](pyatool/extras.py).

And, some [demo](demo.py).

## Install

support python3 only

```python
pip install pyatool
```

## Goal

Easy way to handle android devices with python

## Need more functions?

If you want to execute `adb shell pm list package` to check your installed packages, you can:

```python
# ALL you need
PYAToolkit.bind_cmd(func_name='show_package', cmd='shell pm list package')

# and you can use it
device_toolkit = PYAToolkit('123456F')
result = device_toolkit.show_package()

# it will do:
adb -s 123456F shell pm list package
```

Say goodbye to `subprocess.Popen` :)

If you need a complex function:

```python
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


PYAToolkit.bind_func(real_func=download_and_install)
```

and then you can use it:

```python
device_toolkit = PYAToolkit('123456F')
device_toolkit.download_and_install()
```

## Suggestion or Contribution?

Welcome issue & PR :)

## License

MIT
