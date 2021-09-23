from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in donate/__init__.py
from donate import __version__ as version

setup(
	name='donate',
	version=version,
	description='A portal for donation',
	author='chezuba',
	author_email='abc@chezuba.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
