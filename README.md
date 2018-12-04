# pyatool

[English Version](https://github.com/williamfzc/pyatool/blob/master/README_en.md)

[![Maintainability](https://api.codeclimate.com/v1/badges/5f6647a3121aa7d278ab/maintainability)](https://codeclimate.com/github/williamfzc/pyatool/maintainability)
[![PyPI version](https://badge.fury.io/py/pyatool.svg)](https://badge.fury.io/py/pyatool)
[![Downloads](https://pepy.tech/badge/pyatool)](https://pepy.tech/project/pyatool)

> python android toolkit 🔨

## 目标

- 简化日常开发中对设备的操作
- 简洁的方法自定义与增删
- 无痛融入到现有框架内
- 减少重复工作，共享开发
- 降低使用门槛，让所有人都可以快速上手

## 设计与使用

### 导入

```python
from pyatool import PYAToolkit
```

### 自定义函数

pyatool提供的自定义API让开发者能够很方便地自定义需要的方法并挂载到上面。事实上，它自带的方法也是通过这种方法开发的。

#### 简单定制

例如，我们想自定义一个方法`show_package`用于展示已安装的包并做进一步处理：

```python
# 自定义需要的函数，传入名称与对应的adb命令
PYAToolkit.bind_cmd(func_name='show_package', cmd='shell pm list package')

# 初始化
device_toolkit = PYAToolkit('123456F')

# 然后你就可以直接使用了：
result = device_toolkit.show_package()

# 它将执行下列命令并将执行结果返回到result：
adb -s 123456F shell pm list package
```

再也不用看到那些烦人的`os`与`subprocess`。pyatool也覆盖了多台设备同时连接时的状况，所有烦人的`adb -s 123456F shell`再见~

#### 高级定制

当然，我们平时的需求不可能仅仅需要一条adb命令。pyatool也支持了更复杂的定制。例如我们需要一个函数，用于下载apk并安装到手机上：

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

pyatool如此设计的目的是为了能够尽量减少重复工作。为了方便所有人加入开发，往内置库中添加方法非常容易。

如果你编写了一些好方法并希望将其合入pyatool内置库以方便后续使用，你只需要：

- 直接在github上编辑`extras.py`
- 将写好的函数按照格式粘贴到`extras.py`中
- 在`__all__`中加入你的函数名称
- 描述你的修改，然后点击`Propose file change`，github会自动为你发起pull request

要让库变得更方便好用还是需要各位的共同努力~

## 具体案例

在实际开发中，我们可能会频繁给设备安装apk；例如一旦设备连入电脑，自动给该设备安装apk。而结合[whenconnect](https://github.com/williamfzc/whenconnect)，只需要几行代码就可以实现：

```python
from pyatool import PYAToolkit
from whenconnect import when_connect, start_detect


VERSION = 'v0.1.4'
BASE_URL = r'https://github.com/williamfzc/simhand2/releases/download/{}/{}'
TEST_APK = r'app-debug-androidTest.apk'
MAIN_APK = r'app-debug.apk'

TEST_DL_URL = BASE_URL.format(VERSION, TEST_APK)
MAIN_DL_URL = BASE_URL.format(VERSION, MAIN_APK)


def install_sh(device_id):
    pya = PYAToolkit(device_id)
    pya.install_from(url=TEST_DL_URL)
    pya.install_from(url=MAIN_DL_URL)
    print('install simhand2 ok in {}'.format(device_id))


when_connect(device='all', do=install_sh)
start_detect()
```

就完成了。在运行之后，一旦有android设备接入，将会自动为其安装apk。

## API

pyatool本身提供了丰富的（并没有）标准函数库供开发者直接使用，已经有的函数就不需要再次编写了。

同时也欢迎热心人士为标准库添砖加瓦，无论是提出修改意见或者新增方法 :) 已有的函数很可能难以适应不同的情况。

使用方法推荐直接看代码：

- demo：[demo.py](https://github.com/williamfzc/pyatool/blob/master/demo.py)
- API：[extras.py](https://github.com/williamfzc/pyatool/blob/master/pyatool/extras.py)

## 安装

```python
pip install pyatool
```

## TODO

- [ ] 用subprocess调用adb的方式依旧不够科学，参考[socket2adb](https://github.com/williamfzc/socket2adb)
- [ ] 标准函数库因为动态绑定导致在IDE中没有自动补全

## 意见与建议

欢迎issue与PR

## 协议

MIT
