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

### custom

```python
PYAToolkit.bind(func_name='show_package', cmd='shell pm list package')
device_toolkit = PYAToolkit('123456F')

# and you can:
result = device_toolkit.show_package()

# will run:
# adb -s 123456F shell pm list package
```

and the 'result' will be the result of adb command.
