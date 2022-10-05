#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(name='IO_FILE',
    version="0.1.0",
    description='easy to exploit IO_FILE',
    author='rycbar',
    author_email='rycbar17th@gmail.com',
    maintainer='rycbar',
    maintainer_email='rycbar17th@gmail.com',
    url='blog.rycbar.club',
    packages=find_packages(),
    install_requires=[
        'pwntools'
              ],
    # long_description="easy to libc source code debug and make breakpoint.",
    license="Public domain",
    platforms=["any"],
    )
