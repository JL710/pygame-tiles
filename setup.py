from setuptools import setup
import setuptools

setup(
	name='pygametiles',
	version='0.0.1',
	description='tilesystem for pygame',
	py_modules=["pygametiles"],
	package_dir={'': 'src'},
	packages=setuptools.find_packages(where="src")
)