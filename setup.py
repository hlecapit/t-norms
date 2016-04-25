#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

version = "0.1"
setup(name='t-norms',
      version=version,
      description='Python implementations of triangular norms and related operators',
      author=['Hoel Le Capitaine'],
      author_email='hoel.lecapitaine@univ-nantes.fr',
      url='http://github.com/hlecapit/t-norms',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering'
      ],
      packages=['metric_learn'],
      install_requires=[
          'numpy',
          'scipy'
      ],
      extras_require=dict(
          docs=['sphinx', 'numpydoc'],
          demo=['matplotlib'],
      ),
      test_suite='test',
      keywords=[
          'Triangular norms',
          'Aggregation operators',
          'Fuzzy logic'
      ])
