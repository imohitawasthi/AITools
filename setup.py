#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'matplotlib', 'pandas']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Mohit Awasthi",
    author_email='imohitawasthi@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Artificial Intelligence Tool Kit Mark Two.",
    entry_points={
        'console_scripts': [
            'aitools=aitools.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aitools',
    name='aitools',
    packages=find_packages(include=['aitools', 'aitools.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/imohitawasthi/aitools',
    version='0.2.0',
    zip_safe=False,
)
