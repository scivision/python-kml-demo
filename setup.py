#!/usr/bin/env python3

from setuptools import setup
import subprocess

try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))


with open('README.rst','r') as f:
	long_description = f.read()

setup(name='python-kml-demo',
      version='0.1',
	  description='Demo of making KML from Python',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/python-kml-demo',
	  install_requires=['simplekml'],
      dependency_links = [],
      packages=['python-kml-demo'],
	  )

