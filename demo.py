from pyatool import PYAToolkit


# 个性化的函数需要toolkit形参，即使不需要使用
def test_b(toolkit):
    return 'i am test_b, running on {}'.format(toolkit.device_id)


# 封装adb命令成为方法
PYAToolkit.bind_cmd(func_name='test_a', command='shell pm list package | grep google')
# 或者绑定个性化的函数
PYAToolkit.bind_func(real_func=test_b)

# 修改配置
PYAToolkit.change_conf('TAG_EXEC_CMD', 'EXEC_COMMAND')

# 是否需要log
PYAToolkit.switch_logger(True)

# 初始化
d = PYAToolkit('123456F')

# 它也支持远程控制（还不够稳定，暂不推荐
# d = PYAToolkit('123456F', mode='remote')

# 已经绑定的方法直接调用即可
result = d.test_a()
# output (may be different)
# package:com.google.android.webview

# 个性化函数也一样
result = d.test_b()
# i am test_b, running on 123456F

# 可以通过`standard_func`查询已有的标准函数（会有代码自动补全，比较方便），但不要通过它调用
# d.standard_func.get_current_activity()
# 应该直接这么调用
d.get_current_activity()

# 获取所有已经注册的函数
all_functions = d.current_function()
print(all_functions)

# 下面列举所有标准函数的使用方法，有任何问题欢迎反馈或自己改
# test-only
d.hello_world()

# 展示所有已安装的包
installed_package = d.show_package()

# 栈顶活动名
current_activity_name = d.get_current_activity()

# 安装指定apk（支持url与path），例子里的安装可能比较久因为是从github下的，可以自己改
d.install_from(url=r'https://github.com/williamfzc/simhand2/releases/download/v0.1.2/app-debug.apk')
# d.install_from(path=r'/Users/admin/some_path/some_apk.apk')

# 检测包是否已安装
target_package_name = 'com.github.williamfzc.simhand2'
is_installed = d.is_installed(package_name=target_package_name)

# 清理缓存
d.clean_cache(target_package_name)
if is_installed:
    d.uninstall(target_package_name)

# 获取手机ip
local_address = d.get_ip_address()
print(local_address)

# 切换wifi状态
d.switch_wifi(False)
# 切换飞行模式
d.switch_airplane(True)
d.switch_airplane(False)
d.switch_wifi(True)

# 切换输入法
d.set_ime('com.sohu.inputmethod.sogouoem/.SogouIME')

# push and pull
d.push('./README.md', '/sdcard/')
d.pull('/sdcard/README.md', './haha.md')

# stop app
d.clean_backstage()

# send keyevent
d.input_key_event(26)
d.input_key_event(26)

# swipe
d.swipe(500, 1200, 500, 200)
