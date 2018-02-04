targets = \
  clean \
  code-check \
  coverage \
  coverage-html \
  help \
  install \
  package \
  shell \
  test \
  uninstall \


.PHONY: $(targets)


target_help = \
  "clean - Shutdown all running containers and removes data files." \
  "code-check - Runs Flake8 and pycodestyle on the files changed between the " \
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
  "shell - Start Django shell that can load this package." \
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

DEV_PACKAGES = ipython pycodestyle flake8 coverage tox mock \
  factory-boy # factory-boy is in setup.py, but is not getting loaded
  

DJANGO_VERSION = 1.10.8
VENV = venv
ACTIVATE = $(VENV)/bin/activate

$(VENV): requirements.txt Makefile
	@pip install virtualenv
	@rm -rf $(VENV)
	@virtualenv -p `which python3` $@
	@touch $(ACTIVATE)
	@. $(ACTIVATE) ; \
	DJANGO_VERSION=$(DJANGO_VERSION) pip install -r requirements.txt; \
	  pip install $(DEV_PACKAGES)

package: $(VENV)
	@. $(ACTIVATE); python setup.py sdist

clean:
	@rm -rf $(VENV) django_accelerator.egg-info dist

code-check: $(VENV)
	@. $(ACTIVATE); \
	git diff --name-only development | grep __init__.py | \
	xargs $(XARGS_FLAG) pycodestyle --ignore E902; \
	git diff --name-only development | grep "\.py" | \
	grep -v __init__.py | grep -v 0001_initial.py | \
	xargs $(XARGS_FLAG) flake8

coverage: coverage-run coverage-report coverage-html

coverage-run: $(VENV)
	@. $(ACTIVATE); \
	DJANGO_SETTINGS_MODULE=settings coverage run \
	--omit="*/tests/*,*/venv/*" --source='.' \
	/usr/local/bin/django-admin.py test


BRANCH ?= development

coverage-report: diff_files:=$(shell git diff --name-only $(BRANCH))
coverage-report: diff_sed:=$(shell echo $(diff_files)| sed s:web/impact/::g)
coverage-report: diff_grep:=$(shell echo $(diff_sed) | tr ' ' '\n' | \
  grep \.py | grep -v /tests/ | grep -v /venv/ | \
  grep -v /django_migrations/ | grep -v setup.py | tr '\n' ' ' )
coverage-report: $(VENV)
	@. $(ACTIVATE); DJANGO_SETTINGS_MODULE=settings \
	coverage report --skip-covered $(diff_grep) | grep -v "NoSource:"

coverage-html: $(VENV)
	@. $(ACTIVATE); DJANGO_SETTINGS_MODULE=settings \
	coverage html --omit="*/tests/*,*/venv/*"

coverage-html-open: coverage-html
	@open htmlcov/index.html

install: package uninstall
	pip install dist/*

uninstall:
	-pip uninstall -qy django-accelerator

migrations: $(VENV)
	@. $(ACTIVATE); DJANGO_VERSION=$(DJANGO_VERSION) \
	DJANGO_SETTINGS_MODULE=settings \
	django-admin.py makemigrations accelerator
	@. $(ACTIVATE); DJANGO_VERSION=$(DJANGO_VERSION) \
	DJANGO_SETTINGS_MODULE=settings \
	django-admin.py makemigrations simpleuser

migrate: $(VENV)
	@. $(ACTIVATE); DJANGO_SETTINGS_MODULE=settings \
	django-admin.py migrate $(APPLICATION) $(MIGRATION)

shell: $(VENV)
	@. $(ACTIVATE); DJANGO_SETTINGS_MODULE=settings django-admin.py shell

test: $(VENV)
	@. $(ACTIVATE); DJANGO_SETTINGS_MODULE=settings django-admin.py test $(TESTS)

tox: $(VENV)
	@. $(ACTIVATE); tox

