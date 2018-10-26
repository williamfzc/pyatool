# pyat

> python android toolkit

## Target

- 简化日常开发中对设备的操作
- 插件式

## Design

### import

```python
from pyat import PYAToolkit
```

### usage

```python
device_toolkit = PYAToolkit('123456F')
device_toolkit.some_func(some_arg)

# some built-in functions
device_toolkit.download_and_install('abc.apk')
```

### custom

```python
device_toolkit = PYAToolkit('123456F')
device_toolkit.bind(func_name='show_package', cmd='pm list package', shell=True)

# and you can:
device_toolkit.show_package()
# will run:
# adb -s 123456F shell pm list package
```
