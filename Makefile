targets = \
  help \
  \
  test \
  tox \
  coverage \
  coverage-html \
  code-check \
  \
  update-schema \
  data-migration \
  migrations \
  \
  status \
  checkout \
  \
  clean \
  \
  run-all-servers \
  stop-all-servers \
  shutdown-all-vms \
  delete-all-vms \


IMPACT_API = ../impact-api
IMPACT_MAKE = cd $(IMPACT_API) && $(MAKE)
ACCELERATE = ../accelerate
ACCELERATE_MAKE = cd $(ACCELERATE) && $(MAKE)


.PHONY: $(targets)


target_help = \
  'help - Prints this help message.' \
  ' ' \
  'test - Run tests with no coverage. Run just those specified in $$(tests)' \
  '\tif provided.  E.g.:' \
  '\tmake test tests="impact.tests.test_file1 impact.tests.test_file2"' \
  'coverage - Run tests with coverage summary in terminal.' \
  'coverage-html - Run tests with coverage and open report in browser.' \
  'code-check - Runs Flake8 and pycodestyle on the files changed between the' \
  '\tcurrent branch and $$(branch) (defaults to $(DEFAULT_BRANCH))' \
  'tox - Run tox to run tests on all supported configurations.' \
  ' ' \
  'update-schema - Brings database schema up to date.  Specifically,' \
  '\tupdates any model definitions managed in other libraries,' \
  '\tcreates any needed migrations (uses $$(migration_name) if provided),' \
  '\truns any pending migrations.' \
  'data-migration - Create empty migration.' \
  '\tUses $$(migration_name) if provided.' \
  'migrations - Create any needed auto-generated migrations.' \
  '\tUses $$(migration_name) if provided.' \
  'migrate - Runs migrations. If $$(migration) is given then then that ' \
  '\tmigration is targeted in the accelerator package unless another ' \
  '\t$$(application) is given.  Examples:' \
  '\taccelerate 0123: make migrate migration=0123' \
  '\tsimpleuser 0123: make migrate migration=0123 application=simpleuser' \
  ' ' \
  'status - Reports the status of all related source code repositories.' \
  'checkout - Switch all repos to $(DEFAULT_BRANCH) (or $$(branch)' \
  '\tif provided and available) and pulls down any changes to the branch.' \
  '\tReports any errors from the different repos.' \
  ' ' \
  'clean - Clean out all build products.' \
  ' ' \
  'run-all-servers - Starts a set of related servers.' \
  'stop-all-servers - Stops a set of related servers.' \
  'shutdown-all-vms - Shutdown set of related server VMs' \
  'delete-all-vms - Deletes set of related server VMs' \
  ' ' \
  'release-list - List all releases that are ready to be deployed.' \
  'deploy - Deploy $$(release_name) to a $$(target).' \
  '\tValid targets include "staging" (the default), "production",' \
  '\t "test-1", and "test-2"' \
  ' ' \
  '\t scripts/run_make_commands_in_docker.sh, however it also can run in the' \
  '\t accelerator container' \
  'build - Builds the Docker image for django_accelerator' \
  'setup - Sets up a Docker testing environent for django_accelerator' \
  'stop-server - Stops the Docker testing environent for django_accelerator' \
  'run - runs Makefile commands inside the Docker container.' \
  '\tSet the "command" variable e.g. `make run command=test`' \
  "bash-shell - Allows getting into the django_accelerator container's terminal" \

OS = $(shell uname)

ifeq ($(OS), Linux)
	XARGS_FLAG = -r
endif

help:
	@echo "Valid targets are:\n"
	@for t in $(target_help) ; do \
	    echo $$t; done
	@echo


DJANGO_VERSION = 2.2.10
VENV = venv
ACTIVATE_SCRIPT = $(VENV)/bin/activate
ACTIVATE = export PYTHONPATH=.; . $(ACTIVATE_SCRIPT)
DJANGO_ADMIN = $(VENV)/bin/django-admin.py
PYTHON_VERSION = python3


$(VENV): requirements/base.txt requirements/dev.txt Makefile
	@if ! eval $(PYTHON_VERSION) --version ; then \
		echo "You need to install $(PYTHON_VERSION) for this to work.."; exit 1; \
	fi
	@pip install virtualenv
	@rm -rf $(VENV)
	@virtualenv -p `which $(PYTHON_VERSION)` $@
	@cp git-hooks/* .git/hooks/
	@touch $(ACTIVATE_SCRIPT)
	@$(ACTIVATE) ; \
	DJANGO_VERSION=$(DJANGO_VERSION) pip install -r requirements/dev.txt

package: $(VENV)
	@$(ACTIVATE); python setup.py sdist

clean:
	@rm -rf $(VENV) django_accelerator.egg-info dist

code-check: $(VENV)
	@$(ACTIVATE); \
	git diff --name-only development | grep __init__.py | \
	xargs $(XARGS_FLAG) pycodestyle --ignore E902; \
	git diff --name-only development | grep "\.py" | \
	grep -v __init__.py | grep -v 0001_initial.py | \
	xargs $(XARGS_FLAG) flake8

coverage: coverage-run coverage-report coverage-html-report

coverage-run: $(VENV)
	@$(ACTIVATE); \
	DJANGO_SETTINGS_MODULE=settings coverage run \
	--omit="*/tests/*,*/venv/*" --source='.' \
	$(DJANGO_ADMIN) test


DEFAULT_BRANCH = development
branch ?= $(DEFAULT_BRANCH)

coverage-report: diff_files:=$(shell git diff --name-only $(branch))
coverage-report: diff_sed:=$(shell echo $(diff_files)| sed s:web/impact/::g)
coverage-report: diff_grep:=$(shell echo $(diff_sed) | tr ' ' '\n' | \
  grep \.py | grep -v /tests/ | grep -v /venv/ | \
  grep -v /django_migrations/ | grep -v setup.py | tr '\n' ' ' )
coverage-report: $(VENV)
	@$(ACTIVATE); DJANGO_SETTINGS_MODULE=settings \
	coverage report -i --skip-covered $(diff_grep) | grep -v "NoSource:"

coverage-html-report: $(VENV)
	@$(ACTIVATE); DJANGO_SETTINGS_MODULE=settings \
	coverage html --omit="*/tests/*,*/venv/*"

coverage-xml-report: $(VENV)
	@$(ACTIVATE); DJANGO_SETTINGS_MODULE=settings \
	coverage xml --omit="*/tests/*,*/venv/*"

coverage-html: coverage
	@open htmlcov/index.html

install: package uninstall $(VENV)
	@$(ACTIVATE); pip install dist/*

uninstall: $(VENV)
	-@$(ACTIVATE); pip uninstall -qy django-accelerator

ifdef migration_name
	MIGRATION_ARGS = --name $(migration_name)
endif

data-migration: $(VENV)
	@$(ACTIVATE); DJANGO_VERSION=$(DJANGO_VERSION) \
	DJANGO_SETTINGS_MODULE=settings \
	$(DJANGO_ADMIN) makemigrations accelerator --empty $(MIGRATION_ARGS)

migrations: $(VENV)
	@$(ACTIVATE); DJANGO_VERSION=$(DJANGO_VERSION) \
	DJANGO_SETTINGS_MODULE=settings \
	$(DJANGO_ADMIN) makemigrations accelerator $(MIGRATION_ARGS)
	@$(ACTIVATE); DJANGO_VERSION=$(DJANGO_VERSION) \
	DJANGO_SETTINGS_MODULE=settings \
	$(DJANGO_ADMIN) makemigrations simpleuser $(MIGRATION_ARGS)

test: $(VENV)
	@$(ACTIVATE); DJANGO_SETTINGS_MODULE=settings python3 -Wall $(DJANGO_ADMIN) test $(tests)

tox: $(VENV)
	@$(ACTIVATE); tox

release-list release deploy run-all-servers stop-all-servers shutdown-all-vms delete-all-vms status:
	@$(ACCELERATE_MAKE) $@

application ?= accelerator

migrate update-schema:
	@$(IMPACT_MAKE) $@ application=$(application) migration=$(migration)

checkout:
	@$(IMPACT_MAKE) $@ branch=$(branch)

build:
	@docker build -f base.Dockerfile -t accelerator_tests .

setup: build
	@docker-compose up -d

stop-server:
	@docker-compose down

run:
	@docker-compose exec accelerator scripts/run_make_commands_in_docker.sh $(command)

bash-shell:
	@docker-compose exec accelerator /bin/bash
