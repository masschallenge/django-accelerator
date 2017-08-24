targets = \
  clean \
  code-check \
  coverage \
  coverage-html \
  help \
  install \
  package \
  test \
  uninstall \


.PHONY: $(targets)


target_help = \
  "clean - Shutdown all running containers and removes data files." \
  "code-check - Runs Flake8 and pep8 on the files changed between the current branch and and a given BRANCH (defaults to development)" \
  "coverage - Run coverage and generate text report." \
  "coverage-html - Run coverage and generate HTML report." \
  "help - Prints this help message." \
  "install - Builds package and installs it in the local virtualenv." \
  "package - Create python package for this library (default)." \
  "test - Run tests." \
  "uninstall - Removes the package from the local virtuanlenv." \
  "" \
  "Note: various targets automatically create a python virtualenv if needed."

# TODO: Figure out if we can run a single test:
#  "\tmake test TESTS='impact.tests.test_api_routes.TestApiRoute.test_api_object_get impact.tests.test_api_routes.TestApiRoute.test_api_object_delete'"


ENVIRONMENT_NAME = venv
SETUP_ENV = $(ENVIRONMENT_NAME)/bin/activate

package: $(SETUP_ENV)
	@. $(SETUP_ENV); python setup.py sdist

help:
	@echo "Valid targets are:\n"
	@for t in $(target_help) ; do \
	    echo $$t; done
	@echo

DEV_PACKAGES = ipython pep8 flake8 \
  factory-boy # factory-boy is in setup.py, but is not getting loaded

$(SETUP_ENV):
	@pip install virtualenv
	@virtualenv -p `which python3` $(ENVIRONMENT_NAME)
	@. venv/bin/activate ; pip install -r requirements.txt; \
	  pip install $(DEV_PACKAGES)

clean:
	@rm -rf venv django_accelerator.egg-info dist

code-check: $(SETUP_ENV)
	-@. $(SETUP_ENV); \
	git diff --name-only development | grep __init__.py | \
	  xargs pep8 --ignore E902; \
	git diff --name-only development | grep "\.py" | \
	  grep -v __init__.py | xargs flake8

coverage: $(SETUP_ENV)
	@echo $@ not yet implemented

coverage-html:
	@echo $@ not yet implemented

install: package uninstall
	pip install dist/*

uninstall:
	-pip uninstall -qy django-accelerator

migrations: $(SETUP_ENV)
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings django-admin.py makemigrations

test: $(SETUP_ENV)
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings django-admin.py test
