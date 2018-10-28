# pyat

> python android toolkit 🔨

## 目标

- 简化日常开发中对设备的操作
- 简洁的方法自定义与增删
- 无痛融入到现有框架内

## 设计

### 导入

```python
from pyat import PYAToolkit
```

### 自定义函数

pyat提供的自定义API让开发者能够很方便地自定义需要的方法并挂载到pyat上。事实上，自带的方法也是通过这种方法开发的。

#### 简单定制

例如，我们想自定义一个方法`show_package`用于展示已安装的包并做进一步处理：

```python
# 自定义需要的函数，传入名称与对应的adb命令
PYAToolkit.bind(func_name='show_package', cmd='shell pm list package')

# 初始化
device_toolkit = PYAToolkit('123456F')

# 然后你就可以直接使用了：
result = device_toolkit.show_package()

# 它将执行下列命令并将执行结果返回到result：
adb -s 123456F shell pm list package
```

再也不用看到那些烦人的`os`与`subprocess`。pyat也覆盖了多台设备同时连接时的状况，所有烦人的`adb -s 123456F shell`再见~

#### 高级定制

当然，我们平时的需求不可能仅仅需要一条adb命令。pyat也支持了更复杂的定制。例如我们需要一个函数，用于下载apk并安装到手机上：

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

其中，你的函数必须包含名为toolkit的可选参数，它将提供一些方法用于简化开发流程。例如，通过`toolkit.device_id`获取设备id、`toolkit.adb.run`用于执行adb命令。

```python
# 之后就可以自由使用
device_toolkit = PYAToolkit('123456F')
device_toolkit.download_and_install()
```

#### 单次开发

pyat如此设计的目的是为了能够尽量减少重复工作。为了方便所有人加入开发，往pyat内置库中添加方法非常容易。

如果你编写了一些好方法并希望将其合入pyat内置库以方便后续使用，你只需要：

- 将他们按照格式粘贴到`extras.py`中
- 在`__all__`中加入你的函数名称
- 运行，看一下它能否正常运作
- 确认无误后发起PR就可以啦！

要让库变得更方便好用还是需要各位的共同努力~

## 意见与建议

欢迎issue与PR

## 协议

MIT
