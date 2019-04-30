import re

from .utils import (
    remove_leading_slashes_from_strings,
    remove_trailing_slashes_from_strings,
    remove_trailing_and_leading_whitespace,
    remove_leading_hastag_on_valid_twitter_handles,
    remove_twitter_url_prefix_from_handles,
    remove_not_available_abbreviation_from_twitter_handles,
    turn_handles_with_incomplete_handles_to_empty_string
)


def clean_expert_profile_twitter_handles(ExpertProfile):
    remove_twitter_url_prefix_from_handles(ExpertProfile)
    turn_handles_with_incomplete_handles_to_empty_string(ExpertProfile)
    remove_not_available_abbreviation_from_twitter_handles(ExpertProfile)
    remove_leading_hastag_on_valid_twitter_handles(ExpertProfile)

    for ent in ExpertProfile.objects.exclude(twitter_handle=""):
        twitter_handle = ent.twitter_handle
        match = re.match(r'^@?(\w){1,15}$', twitter_handle)
        if not match:
            remove_trailing_and_leading_whitespace(ent)
            remove_leading_slashes_from_strings(ent)
            remove_trailing_slashes_from_strings(ent)
