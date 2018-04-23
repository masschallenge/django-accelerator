# Django-Accelerator

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/masschallenge/impact-api.svg?branch=development)](https://travis-ci.org/masschallenge/django-accelerator)

Accelerator is a simple Django package which provides models for the
MassChallenge Accelerator applications.

The package supports two modes of use, in two different django apps:

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


## Quick start

### As a dependency for MassChallenge's Accelerate/Impact-API

The development environment for Accelerate and [Impact-API](
https://github.com/masschallenge/impact-api/) were configured to use
django-accelerator as an editable source.

Follow the instructions on [Setting Up The Development Environment](
https://github.com/masschallenge/standards/blob/AC-5050/setup_development_environment.md)
for further details.

### As a dependency for a stand-alone django project

1.  Add "accelerator" to your INSTALLED\_APPS setting like this:
    
        INSTALLED_APPS = [
            ...
            'accelerator.apps.AcceleratorConfig',
        ]

2\. Run `python manage.py migrate` 

3\. The new class should now appear in your application's admin and
through the Django shell.

## Development

### Changing A Swappable Model

Since Django-accelerator uses [Swappable Models](
https://github.com/wq/django-swappable-models). changing the django
models is slightly different than usual.

The key differences to note are:

- All the model declarations - django fields, methods, meta configration,
etc. - should live in the respective Base model, inside 
`accelerator_abstract.models`. This makes the changes usable both
by the `accelerator` app, and any app that inherits directly
from `accelerator_abstract` and declares it's own concrete models.
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
- Any use of model that is expected to be swapped, should use
dynamic imports in a similar fashion. Any code that lives inside
`accelerator_abstract` falls under this category.
- `accelerator.tests.factories` module contains all the [Factory-Boy](
http://factoryboy.readthedocs.io/en/latest/) classes for the
django-accelerator models. They must be defined in the concrete
app, since the factories need a concrete class to work with. But in order
for the factories to be swappable as well, they are defined as such:
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

