#!/usr/bin/env python
install_requires = ['numpy','pandas','simplekml',
        'pymap3d']
tests_require=['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pythonKMLdemo',
      packages=find_packages(),
	  description='Demo of making KML from Python',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/python-kml-demo',
      version='0.1.0',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3',
      ],
       install_requires=install_requires,
       python_requires='>=3.6',
       tests_require=tests_require,
       extras_require={'tests':tests_require},
	  )

