#!/usr/bin/env python
req = ['nose','numpy','pandas',]
pipreq=['simplekml','pymap3d']

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)

# %%
from setuptools import setup

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
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      ],
	  )

