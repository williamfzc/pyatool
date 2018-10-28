from setuptools import setup, find_packages


setup(
    name='pyatool',
    version='0.1.1',
    description='python android toolkit',
    author='williamfzc',
    author_email='fengzc@vip.qq.com',
    url='https://github.com/williamfzc/pyatool',
    packages=find_packages(),
    install_requires=[
        'structlog',
    ]
)
