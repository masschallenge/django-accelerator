# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import os

PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            "accelerator"))

TIME_ZONE = 'America/New_York'
USE_TZ = True

INSTALLED_APPS = [
    "django.contrib.auth",
    "simpleuser",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "accelerator_abstract",
    "accelerator",
    "accelerator.tests",
    "embed_video",
]

MIDDLEWARE_CLASSES = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

SITE_ID = 1

ROOT_URLCONF = "accelerator.tests.urls"

SECRET_KEY = "notasecret"

AUTH_USER_MODEL = 'simpleuser.User'

ACCELERATOR_MODELS_ARE_MANAGED = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

TEST_RUNNER = 'accelerator.test_runner.UnManagedModelTestRunner'

MPTT_SWAPPABLE_INDUSTRY_MODEL = "accelerator.Industry"
MPTT_SWAPPABLE_INDUSTRY_MODEL_ADDITIONAL = "accelerator.Industry"
MPTT_SWAPPABLE_INDUSTRY_DB_TABLE_NAME = "accelerator_startup_related_industry"

# Django-Accelerator's Swappable Models configuration
ACCELERATOR_APPLICATION_MODEL = "accelerator.Application"
ACCELERATOR_APPLICATIONANSWER_MODEL = "accelerator.ApplicationAnswer"
ACCELERATOR_APPLICATIONQUESTION_MODEL = "accelerator.ApplicationQuestion"
ACCELERATOR_APPLICATIONTYPE_MODEL = "accelerator.ApplicationType"
ACCELERATOR_CURRENCY_MODEL = "accelerator.Currency"
ACCELERATOR_INDUSTRY_MODEL = "accelerator.Industry"
ACCELERATOR_JOBPOSTING_MODEL = "accelerator.JobPosting"
ACCELERATOR_NAMEDGROUP_MODEL = "accelerator.NamedGroup"
ACCELERATOR_ORGANIZATION_MODEL = "accelerator.Organization"
ACCELERATOR_PROGRAM_MODEL = "accelerator.Program"
ACCELERATOR_PROGRAMCYCLE_MODEL = "accelerator.ProgramCycle"
ACCELERATOR_PROGRAMFAMILY_MODEL = "accelerator.ProgramFamily"
ACCELERATOR_QUESTION_MODEL = "accelerator.Question"
ACCELERATOR_RECOMMENDATIONTAG_MODEL = "accelerator.RecommendationTag"
ACCELERATOR_STARTUP_MODEL = "accelerator.Startup"
ACCELERATOR_STARTUPLABEL_MODEL = "accelerator.StartupLabel"
