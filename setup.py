#!/usr/bin/env python
from setuptools import setup

req = ['nose','numpy','pandas',
       'simplekml','pymap3d']

setup(name='pythonKMLdemo',
      packages=['python-kml-demo'],
	  description='Demo of making KML from Python',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/python-kml-demo',
      version='0.1',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      ],
	  install_requires=req,
	  )

