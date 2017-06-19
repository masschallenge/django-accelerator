# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-accelerator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A Django app to provide MassChallenge Accelerator models.',
    long_description=README,
    url='http://masschallenge.org/',
    author='MassChallenge, Inc.',
    author_email='engineering@masschallenge.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        # Add 1.8 when accelerate is using this
        # Add 1.10 when impact-api is using this
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Add 2.7 when accelerate is using this
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
