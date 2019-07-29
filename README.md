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

### Changing A Swappable Model

Since Django-accelerator uses [Swappable Models](
https://github.com/wq/django-swappable-models). changing the Django
models is slightly different than usual.

**The key differences to note are:**

- All the model declarations - Django fields, methods, meta configration,
etc. - should live in the respective Base model, inside 
`accelerator_abstract.models`. This makes the changes usable both
by the `accelerator` app, and any app that inherits directly
from `accelerator_abstract` and declares its own concrete models.
- The Concrete model in `accelerator` should have no other role
but:
   - to be a concrete subclass of a base model.
   - to declare the `Meta.swappable` configuration.
 
  E.g. the Startup model looks like this:
  ```
  # accelerator/models/startup.py
  import swapper
  from accelerator_abstract.models import BaseStartup
  
  
  class Startup(BaseStartup):
     class Meta(BaseStartup.Meta):
         swappable = swapper.swappable_setting(BaseStartup.Meta.app_label,
                                               'Startup')
  ```
- Model relationships are declared in such a way that allows them to 
be swappable. E.g:
  ```
  # accelerator_abstract/models/base_startup.py
  ...
    primary_industry = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),  
  ...
  ```
- Whenever using models that are expected to be swapped, you should use
dynamic imports in a similar fashion. Any code that lives inside
`accelerator_abstract` falls under this category.
  
  e.g.:
  ```
  # accelerator_abstract/apps.py
  ...
  import swapper
  ...
  BaseProfile = swapper.load_model(AcceleratorConfig.name, 'BaseProfile')
  ```
- `accelerator.tests.factories` module contains all the [Factory-Boy](
http://factoryboy.readthedocs.io/en/latest/) classes for the
django-accelerator models. They must be defined in the concrete
app, since the factories need a concrete class to work with. But in order
for the factories to be swappable as well, they also use dynamic imports:
  ```
  # accelerator/tests/factories/currency_factory.py
  import swapper
  ...
  Currency = swapper.load_model(AcceleratorConfig.name, 'Currency')
  ...
  class CurrencyFactory(DjangoModelFactory):
    class Meta:
        model = Currency
  ```
  So instead of importing `Currency` directly, it is imported dynamically.
  This allowes us to use the same factory class for custom models (as
  long as the custom model doesn't change the abstract fields, but
  only changes methods or Meta configrurations).
- Migrations can be made swappable as well, but they are not
generated correctly by Django, and require slighlty changing the 
auto-generated migration, according to the instructions in
[Django-swappable-models](https://github.com/wq/django-swappable-models).
This feature is not promised to be supported in this repo.

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

This package supports two Django projects:
- 'accelerate', which runs on Python 2.7 and Django 1.11
- 'impact-api', which runs on Python 3.6 and Django 1.10

Therefore, the code must be compatible for both versions,
and the Travis builds are configured to test both.

To test this locally, it is possible to run `make tox`.

Also, Running `make test` will simply run the tests
under the makefile's default Python+[Django](
https://github.com/masschallenge/django-accelerator/blob/development/Makefile#L94)
versions.

---
Copyright 2018, MassChallenge, Inc., some rights reserved
Public license: MIT
