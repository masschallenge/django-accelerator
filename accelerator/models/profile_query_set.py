# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet

from accelerator_abstract.models.base_base_profile import (
    ENTREPRENEUR_USER_TYPE,
    EXPERT_USER_TYPE,
    MEMBER_USER_TYPE,
)
from accelerator.apps import AcceleratorConfig

import swapper

EntrepreneurProfile = swapper.load_model(AcceleratorConfig.name,
                                         "EntrepreneurProfile")
ExpertProfile = swapper.load_model(AcceleratorConfig.name,
                                   "ExpertProfile")
MemberProfile = swapper.load_model(AcceleratorConfig.name,
                                   "MemberProfile")
BaseProfile = swapper.load_model(AcceleratorConfig.name,
                                 "BaseProfile")
User = get_user_model()

logger = logging.getLogger(__file__)

EMAIL_KEY = 'email'
PK_KEY = 'pk'

PROFILE_CLASSES_AND_TYPES = [
    (ExpertProfile, EXPERT_USER_TYPE),
    (EntrepreneurProfile, ENTREPRENEUR_USER_TYPE),
    (MemberProfile, MEMBER_USER_TYPE)
]

MISSING_PROFILE_TEMPLATE = ("No CoreProfile Subclass found. Creating a "
                            "default profile of type '{}'")

INCORRECT_USER_TYPE_TEMPLATE = ("Incorrect user_type found. "
                                "Fixing from '{}' to '{}'")


class ProfileQuerySet(QuerySet):
    """return the appropriate user profile type given user_type"""

    def get(self, *args, **kwargs):
        if PK_KEY in kwargs.keys():
            self.user = User.objects.get(pk=kwargs[PK_KEY])
        elif EMAIL_KEY in kwargs.keys():
            self.user = User.objects.get(email=kwargs[EMAIL_KEY])

        profile_manager = self._profile_manager_by_user_type()

        profile = self._profile_for_inferred_profile_type(profile_manager)
        if profile:
            return profile

    def _profile_manager_by_user_type(self):
        try:
            self.base_profile = BaseProfile.manager.get(user=self.user)
        except ObjectDoesNotExist:
            self.base_profile = None
            return None
        profile_managers = {user_type: kls.objects for
                            kls, user_type in PROFILE_CLASSES_AND_TYPES}
        return profile_managers.get(self.base_profile.user_type, None)

    def _profile_for_inferred_profile_type(self, profile_manager):
        if profile_manager is None:
            return None
        profile = profile_manager.using(self._db).filter(user=self.user).first()
        if not profile:
            profile = self._get_profile_from_existing_profile_types()
        return profile

    def _get_profile_from_existing_profile_types(self):
        for kls, user_type in PROFILE_CLASSES_AND_TYPES:
            profile = kls.objects.using(self._db).filter(
                user=self.user).first()
            if profile:
                self._update_user_type(user_type)
                return profile
        return None

    def _update_user_type(self, user_type):
        logger.warning(INCORRECT_USER_TYPE_TEMPLATE.format(
            self.base_profile.user_type or "", user_type))
        self.base_profile.user_type = user_type
        self.base_profile.save()
