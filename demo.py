from pyat import PYAToolkit


# real function should contains an argument named 'toolkit'
def test_b(toolkit):
    return 'i am test_b, running on {}'.format(toolkit.device_id)


# bind adb command
PYAToolkit.bind_cmd(func_name='test_a', command='shell pm list package | grep google')
# or a real function
PYAToolkit.bind_func(real_func=test_b)

# init
d = PYAToolkit('123456F')

# and call it
result = d.test_a()
print(result)
# output (may be different)
# package:com.google.android.webview

# and call it too
result = d.test_b()
print(result)
# i am test_b, running on 123456F
