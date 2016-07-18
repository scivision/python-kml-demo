#!/usr/bin/env python

from setuptools import setup
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass

setup(name='python-kml-demo',
	  description='Demo of making KML from Python',
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/python-kml-demo',
	  install_requires=['simplekml','pymap3d'],
      dependency_links = ['https://github.com/scienceopen/pymap3d/tarball/master#egg=pymap3d',],
      packages=['python-kml-demo'],
	  )

