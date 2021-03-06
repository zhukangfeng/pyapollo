# encoding: utf-8
"""
pyapollo 常用工具包


"""
from setuptools import setup, find_packages

SHORT=u'pyapollo'
__version__ = '0.1.0'
__author__ = 'filamoon'
__email__ = 'filamoon@gmail.com'

setup(
    name='pyapollo',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests==2.20.1',
        'eventlet==0.24.1'
    ],
    url='https://code.aliyun.com/cashbusrisk/pyapollo',
    author=__author__,
    author_email='filamoon@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    package_data={'': ['*.py','*.pyc']},
    zip_safe=False,
    platforms='any',

    description=SHORT,
    long_description=__doc__,
)
