# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import os
import sys
import logging
from django.db.backends.mysql.base import DatabaseWrapper

DatabaseWrapper.data_types['DateTimeField'] = 'datetime'

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.WARNING)

PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            "accelerator"))

TIME_ZONE = 'America/New_York'
USE_TZ = True

INSTALLED_APPS = [
    "django.contrib.auth",
    "simpleuser.apps.SimpleuserConfig",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "accelerator_abstract.apps.AcceleratorAbstractConfig",
    "accelerator.apps.AcceleratorConfig",
    "accelerator.tests",
    "embed_video",
    "paypal.pro",
    "fluent_pages",
    "sitetree",
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

BULLET_TRAIN_API_KEY = os.environ.get(
    "BULLET_TRAIN_API_KEY", 'aX45EUqSsAqhTvv5nW7WEL')

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
FLUENT_PAGES_TEMPLATE_DIR = PACKAGE_ROOT
TEST_RUNNER = 'accelerator.test_runner.UnManagedModelTestRunner'

MPTT_SWAPPABLE_INDUSTRY_MODEL = "accelerator.Industry"
MPTT_SWAPPABLE_INDUSTRY_MODEL_ADDITIONAL = "accelerator.Industry"
MPTT_SWAPPABLE_FUNCTIONALEXPERTISE_MODEL = "accelerator.FunctionalExpertise"

# Django-Accelerator's Swappable Models configuration
ACCELERATOR_APPLICATION_MODEL = "accelerator.Application"
ACCELERATOR_APPLICATIONANSWER_MODEL = "accelerator.ApplicationAnswer"
ACCELERATOR_APPLICATIONPANELASSIGNMENT_MODEL = (
    "accelerator.ApplicationPanelAssignment")
ACCELERATOR_APPLICATIONQUESTION_MODEL = "accelerator.ApplicationQuestion"
ACCELERATOR_APPLICATIONTYPE_MODEL = "accelerator.ApplicationType"
ACCELERATOR_CURRENCY_MODEL = "accelerator.Currency"
ACCELERATOR_INDUSTRY_MODEL = "accelerator.Industry"
ACCELERATOR_INTERESTCATEGORY_MODEL = "accelerator.InterestCategory"
ACCELERATOR_JOBPOSTING_MODEL = "accelerator.JobPosting"
ACCELERATOR_NAMEDGROUP_MODEL = "accelerator.NamedGroup"
ACCELERATOR_ORGANIZATION_MODEL = "accelerator.Organization"
ACCELERATOR_PANEL_MODEL = "accelerator.Panel"
ACCELERATOR_PANELTIME_MODEL = "accelerator.PanelTime"
ACCELERATOR_PANELTYPE_MODEL = "accelerator.PanelType"
ACCELERATOR_PANELLOCATION_MODEL = "accelerator.PanelLocation"
ACCELERATOR_PROGRAM_MODEL = "accelerator.Program"
ACCELERATOR_PROGRAMCYCLE_MODEL = "accelerator.ProgramCycle"
ACCELERATOR_PROGRAMFAMILY_MODEL = "accelerator.ProgramFamily"
ACCELERATOR_QUESTION_MODEL = "accelerator.Question"
ACCELERATOR_STARTUP_MODEL = "accelerator.Startup"
ACCELERATOR_SCENARIO_MODEL = "accelerator.Scenario"
ACCELERATOR_STARTUPLABEL_MODEL = "accelerator.StartupLabel"
ACCELERATOR_STARTUPATTRIBUTE_MODEL = "accelerator.StartupAttribute"
ACCELERATOR_PAYPALPAYMENT_MODEL = "accelerator.PayPalPayment"
ACCELERATOR_LEGALCHECK_MODEL = "accelerator.LegalCheck"
ACCELERATOR_USERLEGALCHECK_MODEL = "accelerator.UserLegalCheck"
ACCELERATOR_GENDERCHOICES_MODEL = "accelerator.GenderChoices"
ACCELERATOR_ETHNORACIALIDENTITY_MODEL = "accelerator.EthnoRacialIdentity"

PAYPAL_WPP_USER = ""
PAYPAL_WPP_PASSWORD = ""
PAYPAL_WPP_SIGNATURE = ""

CMS_FILE_ROOT = '/var/www/cms-files'
