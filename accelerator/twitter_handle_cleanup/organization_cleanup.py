import re

from .utils import (
    remove_leading_slashes_from_strings,
    remove_trailing_slashes_from_strings,
    remove_trailing_and_leading_whitespace,
    remove_leading_hastag_on_valid_twitter_handles,
    remove_twitter_url_prefix_from_handles,
    remove_not_available_abbreviation_from_twitter_handles,
    remove_hashbang_from_twitter_handles,
    write_to_csv
)


def clean_organization_twitter_handles(Organization):
    remove_twitter_url_prefix_from_handles(Organization)
    remove_not_available_abbreviation_from_twitter_handles(Organization)
    remove_hashbang_from_twitter_handles(Organization)
    remove_leading_hastag_on_valid_twitter_handles(Organization)

    for org in Organization.objects.exclude(twitter_handle=""):
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
        twitter_handle = ""
        if not match:
            match = re.search(
                r'(\?lang)=?([a-zA-z]{1,2})?(-[a-zA-z]{1,2})?',
                org.twitter_handle)
            if match:
                compilation = re.compile(
                    '(\?lang)(=)?([a-zA-z]{1,2})?(-[a-zA-z]{1,2})?')
                found = compilation.findall(org.twitter_handle)
                found_string = ''
                for foundStr in list(found[0]):
                    found_string += foundStr
                old_handle = org.twitter_handle
                new_handle = str(org.twitter_handle).replace(found_string, "")
                org.twitter_handle = new_handle
                org.save()
                write_to_csv(
                    [Organization.__name__, org.id, old_handle, twitter_handle]
                )

            remove_trailing_and_leading_whitespace(org)
            remove_leading_slashes_from_strings(org)
            remove_trailing_slashes_from_strings(org)
