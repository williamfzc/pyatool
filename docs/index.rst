.. fitch documentation master file, created by
   sphinx-quickstart on Wed Feb 20 22:31:44 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyatool's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Usage
=====

使用方法如下 ::

   from pyatool import PYAToolkit

   # 初始化
   device = PYAToolkit('123456F')

   # 1. 直接调用
   package_list = device.show_package()
   # 2. 或者 通过标准库（有自动补全，能够看到真实的方法实现）
   package_list = device.std.show_package(toolkit=device)

   # 具体返回内容与调用的方法实现有关
   print(package_list)

要调用其他的API，将 `show_package` 替换成API名称即可！

API
===
.. automodule:: pyatool.extras
   :members:
   :show-inheritance:
   :undoc-members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
