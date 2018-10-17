#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under the MIT license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import with_statement
from setuptools import setup, Command

def parse_requirements(filename):
    """
    Load requirements from a pip requirements file
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not (line.startswith("#") or line.startswith("-"))]

PACKAGE_NAME = 'skeleton'
PACKAGE_VERSION = '0.2.0'
PACKAGES = ['app']
INSTALL_REQS = [str(req) for req in parse_requirements('requirements/stable.pip')]
TEST_REQS = [str(req) for req in parse_requirements('requirements/dev.pip')]


with open('README.md', 'r') as readme:
    README_TEXT = readme.read()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys
        import subprocess
        opts = []
        if '-v' in sys.argv:
            opts.append('-v')
        errno = subprocess.call([sys.executable, '-m', 'py.test', 'test'] + opts)
        raise SystemExit(errno)


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    packages=PACKAGES,
    description="""Skeleton is a Python Flask template.""",
    long_description=README_TEXT,
    author='Peter Hillerström',
    author_email='peter.hillerstrom@gmail.com',
    license='MIT License',
    url='https://github.com/peterhil/skeleton',
    requires=[
    ],
    install_requires=INSTALL_REQS,
    tests_require=TEST_REQS,
    extras_require={'test': TEST_REQS},
    entry_points={'app': '.test = test'},
    scripts=[],
    classifiers = [
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Topic :: Software Development',
    ],
    cmdclass = {
        'test': PyTest
    },
)
