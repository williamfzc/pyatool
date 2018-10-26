from pyat import PYAToolkit


d = PYAToolkit('123456F')
d.bind(func_name='test_a', command='shell pm list package')
result = d.test_a()
print(result)
