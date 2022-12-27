# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sql_accounting_software/__init__.py
from sql_accounting_software import __version__ as version

setup(
	name="sql_accounting_software",
	version=version,
	description="SQL Accounting Software",
	author="Richard",
	author_email="nabadjarichard@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
