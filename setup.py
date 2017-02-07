#!/usr/bin/env python
from setuptools import setup

try:
    import conda.cli
    conda.cli.main('install','--file','requirements.txt')
except Exception as e:
    print(e)
    import pip
    pip.main(['install','-r','requirements.txt'])


setup(name='pythonKMLdemo',
	  description='Demo of making KML from Python',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scienceopen/python-kml-demo',
      'Intended Audience :: Science/Research',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
	  install_requires=['simplekml','pymap3d'],
      packages=['python-kml-demo'],
	  )

