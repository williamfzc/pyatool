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

device_toolkit.download_and_install('abc.apk')
```
