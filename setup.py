# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

DJANGO_SPEC = ">=1.11,<=2.3"
if "DJANGO_VERSION" in os.environ:
    DJANGO_SPEC = "=={}".format(os.environ["DJANGO_VERSION"])

INSTALL_REQUIRES = [
    "django{}".format(DJANGO_SPEC),
    "django-mptt==0.10.0",
    "sorl-thumbnail",
    "django-embed-video",
    "pillow",
    "pytz",
    "swapper",
    "django-ordered-model==2.1.0",
    "django-paypal==1.0.0",
    "django-fluent-pages==2.0.6",
    "django-polymorphic",
    "django-sitetree==1.12.0"
]

setup(
    name='django-accelerator',
    version='0.2.2',
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
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=INSTALL_REQUIRES,
)
