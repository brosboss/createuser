# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in create_user/__init__.py
from create_user import __version__ as version

setup(
	name='create_user',
	version=version,
	description='!!',
	author='!!',
	author_email='brossboss123@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)