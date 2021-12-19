from setuptools import setup
import setuptools

setup(
	name='pygametiles',
	version='0.0.1',
	description='Simple Tools for Python',
	py_modules=["SimpleTools"],
	package_dir={'': 'src', 'a1': 'a1', 'a2': 'a2'},
)