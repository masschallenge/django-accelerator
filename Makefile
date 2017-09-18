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
  "code-check - Runs Flake8 and pep8 on the files changed between the " \
  "\tcurrent branch and and a given BRANCH (defaults to development)" \
  "coverage - Run coverage and generate text report." \
  "coverage-html - Run coverage and generate HTML report." \
  "help - Prints this help message." \
  "install - Builds package and installs it in the local virtualenv." \
  "migrate - Runs migrations. If MIGRATION is given then then that " \
  "\tmigration is targeted in the accelerator package unless another " \
  "\tAPPLICATION is given. The migrations are run on a temporary" \
  "\tdatabase that is destroyed immediately afterwords." \
  "migrations - Creates an needed migrations due to model changes." \
  "package - Create python package for this library (default)." \
  "test - Run tests. To run a subset of tests:" \
  "\tmake test TESTS='accelerator.tests.test_currency accelerator.tests.test_startup'" \
  "tox - Run tox to run tests on all supported configurations." \
  "uninstall - Removes the package from the local virtuanlenv." \
  "" \
  "Note: various targets automatically create a python virtualenv, venv." \
  "You can us it in your shell by running: 'source venv/bin/activate'"

OS = $(shell uname)

ifeq ($(OS), Linux)
	XARGS_FLAG = -r
endif

ENVIRONMENT_NAME = venv
SETUP_ENV = $(ENVIRONMENT_NAME)/bin/activate
ifdef MIGRATION
ifndef APPLICATION
APPLICATION = accelerator
endif
endif

help:
	@echo "Valid targets are:\n"
	@for t in $(target_help) ; do \
	    echo $$t; done
	@echo

package: $(SETUP_ENV)
	@. $(SETUP_ENV); python setup.py sdist

DEV_PACKAGES = ipython pep8 flake8 coverage tox \
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
	grep accelerator | xargs $(XARGS_FLAG) pep8 --filename accelerator/ --ignore E902; \
	git diff --name-only development | grep accelerator | grep "\.py" | \
	  grep -v __init__.py | xargs $(XARGS_FLAG) flake8 --filename accelerator/

coverage: coverage-run coverage-report coverage-html

coverage-run:
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings coverage run --omit="*/tests/*,*/venv/*" --source='.' /usr/local/bin/django-admin.py test

coverage-report: DIFFBRANCH?=$(shell if [ "${BRANCH}" == "" ]; \
   then echo "development"; else echo "${BRANCH}"; fi;)
coverage-report: diff_files:=$(shell git diff --name-only $(DIFFBRANCH))
coverage-report: diff_sed:=$(shell echo $(diff_files)| sed s:web/impact/::g)
coverage-report: diff_grep:=$(shell echo $(diff_sed) | tr ' ' '\n' | grep \.py | grep -v /tests/ | grep -v /venv/ | grep -v /django_migrations/ | tr '\n' ' ' )
coverage-report:
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings coverage report --skip-covered $(diff_grep) | grep -v "NoSource:"

coverage-html:
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings coverage html --omit="*/tests/*,*/venv/*"

coverage-html-open: coverage-html
	@open htmlcov/index.html

install: package uninstall
	pip install dist/*

uninstall:
	-pip uninstall -qy django-accelerator

migrations: $(SETUP_ENV)
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings django-admin.py makemigrations

migrate: $(SETUP_ENV)
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings django-admin.py migrate $(APPLICATION) $(MIGRATION)

test: $(SETUP_ENV)
	@. $(SETUP_ENV); DJANGO_SETTINGS_MODULE=settings django-admin.py test $(TESTS)

tox: $(SETUP_ENV)
	@. $(SETUP_ENV); tox
