# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages
from io import open

setup(
    name='wechat-sdk',
    version='1.0.0',
    keywords=('wechat', 'sdk', 'wechat sdk'),
    description=u'微信公众平台Python开发包',
    long_description=open("README.rst", encoding="utf-8").read(),
    license='BSD License',

    url='https://gitlab.com/jozzon/wechat-sdk.git',
    author='doraemonext',
    author_email='doraemonext@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    install_requires=list(map(lambda x: x.rstrip('\n').replace('==', '>='), open("requirements.txt", encoding="utf-8").readlines())),

    tests_require=['nose', 'httmock'],
    test_suite='tests',
)
