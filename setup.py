#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
# see LICENSE file (it's MIT)

from io import open
import os
from setuptools import setup

with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pptx-canvas',
    version='0.1',
    description='Canvas-like interface for drawing in PPTX files using Python',
    keywords='powerpoint ppt pptx office open xml',
    long_description=long_description,
    author='Elliott Carlson',
    author_email='x@sublim.nl',
    url='http://github.com/elliottcarlson/pptx-canvas',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['colour','lxml','Pillow','python-pptx','XlsxWriter'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Software Development :: Libraries'
    ]
)
