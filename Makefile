targets = \
  build \
  clean \
  code-check \
  coverage \
  coverage-html \
  help \
  package \
  test \

.PHONY: $(targets)


target_help = \
  "build - Build (or rebuild) docker environment. Refreshes dependencies." \
  "clean - Shutdown all running containers and removes data files." \
  "code-check - Runs Flake8 and pep8 on the files changed between the current branch and and a given BRANCH (defaults to development)" \
  "coverage - Run coverage and generate text report." \
  "coverage-html - Run coverage and generate HTML report." \
  "help - Prints this help message." \
  "package - Create python package for this library." \
  "test - Run tests. To run a single test:"


#  "\tmake test TESTS='impact.tests.test_api_routes.TestApiRoute.test_api_object_get impact.tests.test_api_routes.TestApiRoute.test_api_object_delete'"


ENVIRONMENT_NAME = venv
SETUP_ENV = $(ENVIRONMENT_NAME)/bin/activate

package: $(SETUP_ENV)
	@$(SETUP_ENV); python setup.py sdist

help:
	@echo "Valid targets are:\n"
	@for t in $(target_help) ; do \
	    echo $$t; done
	@echo

PIP_PACKAGES = Django ipython factory-boy django-mptt pep8 flake8 coverage

$(SETUP_ENV):
	@pip install virtualenv
	@virtualenv -p `which python3` $(ENVIRONMENT_NAME)
	@. venv/bin/activate ; pip install $(PIP_PACKAGES)

clean:
	@rm -rf venv django_accelerator.egg-info dist

code-check: $(SETUP_ENV)
	@. $(SETUP_ENV); \
	git diff --name-only development | grep __init__.py | \
	  xargs pep8 --ignore E902; \
	git diff --name-only development | grep "\.py" | \
	  grep -v __init__.py | xargs flake8

coverage: $(SETUP_ENV)
	@echo $@ not yet implemented

coverage-html:
	@echo $@ not yet implemented

migrations: $(SETUP_ENV)
	@. $(SETUP_ENV); python makemigrations.py

test: $(SETUP_ENV)
	@. $(SETUP_ENV); python runtests.py
