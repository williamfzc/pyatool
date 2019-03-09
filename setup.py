from setuptools import setup, find_packages
from pyatool import __VERSION__


setup(
    name='pyatool',
    version=__VERSION__,
    description='python android toolkit',
    author='williamfzc',
    author_email='fengzc@vip.qq.com',
    url='https://github.com/williamfzc/pyatool',
    packages=find_packages(),
    install_requires=[
        'requests',
        'loguru',
    ]
)
