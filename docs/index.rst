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

   device = PYAToolkit('123456F')

   # 直接调用
   package_list = device.show_package()
   # 通过标准库（有自动补全）
   package_list = device.std.show_package(toolkit=device)

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
