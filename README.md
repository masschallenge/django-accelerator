# Django-Accelerator

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/masschallenge/impact-api.svg?branch=development)](https://travis-ci.org/masschallenge/django-accelerator)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2636b03b81f405b133f5/test_coverage)](https://codeclimate.com/github/masschallenge/django-accelerator/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/2636b03b81f405b133f5/maintainability)](https://codeclimate.com/github/masschallenge/django-accelerator/maintainability)

1. [Overview](#overview)
2. [Quickstart](#quickstart)
   1. [As a dependency for MassChallenge's Accelerate/Impact-API](
  #as-a-dependency-for-masschallenges-accelerateimpact-api)
   2. [As a dependency for a stand-alone django project](
   #as-a-dependency-for-a-stand-alone-django-project)
3. [Development](#Development)
   1. [Changing A Swappable Model](#changing-a-swappable-model)
   2. [Generating Migrations](#generating-migrations)
   3. [Running Migrations](#running-migrations)
   4. [Testing](#testing)

Accelerator is a simple Django package which provides models for the
MassChallenge Accelerator applications.

## Overview

The package supports two modes of use, in two different Django apps:

- `accelerator_abstract` - abstract models, declaring all the fields
and relationships between the Base-models. All the models were made to
be swappable,using [Django-swappable-models](
https://github.com/wq/django-swappable-models).
- `accelerator` - regular concrete django models, ready for use. Those
models are the default concrete implementation of the abstract models
defined in `accelerator_abstract`.

The package also includes a third django app, `simpleuser`, that
slightly extends the default django user model. It is also swappable,
in the [usual way](
https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project).


## Quickstart

### As a dependency for MassChallenge's Accelerate/Impact-API

The development environment for Accelerate and [Impact-API](
https://github.com/masschallenge/impact-api/) were configured to use
django-accelerator as an editable source.

Follow the instructions on [Setting Up The Development Environment](
https://github.com/masschallenge/standards/blob/master/setup_development_environment.md)
for further details.

### As a dependency for a stand-alone django project

1.  Add "accelerator" to your INSTALLED\_APPS setting like this:
    
        INSTALLED_APPS = [
            ...
            'accelerator.apps.AcceleratorConfig',
        ]

2\. Run `python manage.py migrate` 

3\. The installed models should now appear in your application's admin and
through the Django shell.

## Development

### Generating Migrations

Running `make migrations` will try to generate new migrations
for `accelerator` and `simpleuser` apps.


### Running Migrations

As this is a package and not a full app, it is impossible
to run stand-alone migrations. The `Makefile` is configured
to run the migrations in the [impact-api](
https://github.com/masschallenge/impact-api/) project in
which this project is installed.

### Testing

To test this locally, it is possible to run `make tox`.

Also, Running `make test` will simply run the tests
under the makefile's default Python+[Django](
https://github.com/masschallenge/django-accelerator/blob/development/Makefile#L94)
versions.

---
Copyright 2019, MassChallenge, Inc., some rights reserved
Public license: MIT
