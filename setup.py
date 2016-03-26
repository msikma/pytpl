#!/usr/bin/env python3
#
# Copyright (C) 2016, Michiel Sikma
# MIT licensed

"""
Installation script. To install for production, run:

    ./setup.py install

When developing, replace 'install' with 'develop'.
"""
from setuptools import setup, find_packages

setup(
    name='pytpl',
    version='1.0.2',
    description='Template for developing Python applications or scripts',
    long_description=(
        'Template designed to make it easy to start developing a Python '
        'application or script with best practices. Includes a proper '
        'example of setup.py.'
    ),
    url='https://github.com/msikma/pytpl',
    author='Michiel Sikma',
    author_email='michiel@sikma.org',
    license='MIT',
    test_suite='pytpl.tests',
    packages=find_packages(),
    install_requires=[
        # terminaltables - for printing tables to the terminal
        # <https://pypi.python.org/pypi/terminaltables/2.1.0>
        'terminaltables >= 2.1.0, < 3.0.0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5'
    ],
    entry_points={
        'console_scripts': [
            'pytpl=pytpl.cli.pytpl:main'
        ]
    },
    zip_safe=True
)
