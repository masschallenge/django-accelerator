===========
Accelerator
===========

Accelerator is a simple Django package which provides models
for the MassChallenge Accelerator applications.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "accelerator" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'accelerator.apps.AcceleratorConfig',
    ]

2. Add a value for `ACCELERATOR_MODELS_ARE_MANAGED` to settings.py for
the different applications.  The intention is for there to be a single
application where the value is True and all other apps using the same
models from the same database set the value to False.

2. Run `python manage.py migrate` in the application that is going to
manage the models to create the accelerator models.

3. The new class should now appear in your application's admin and through
the Django shell.


Moving Models from Impact API
-----------------------------

The set of target models for this package are in the
masschallenge/impact-api repository.  To move a model follow these
steps:

- Copy model and factory from impact-api

- Replace `impact` with `accelerator`.

- Replace `mc` with `accelerator`

- Update __init__.py.  Copy imports for that model from
  `impact-api/web/impact/impact/models/__init__.py` to
  `accelerator/models/__init__.py`

- If needed, update new model definition to include:
  `from django.conf import settings`

- Remove is_managed import.  Replace call to is_managed with
  `settings.ACCELERATOR_MODELS_ARE_MANAGED`

- Check to see if there are any weird conditionals and see about
  adding needed libraries to `PIP_PACKAGES` in the
  `django-accelerator/Makefile` and any needed applications to
  `shared_settings.py`

- Run `make clean`

- Run `make migrations`

- Run `make migrate`

- Run `make test`

- Run `make install`

- Add the new files and checkin the changes.
