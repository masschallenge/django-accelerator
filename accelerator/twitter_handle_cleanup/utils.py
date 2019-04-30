import re
import csv

from django.db.models import (
    F,
    Func,
    Value
)


TWITTER_HANDLE_CSV_FILE_NAME = 'twitter_handle_cleanup.csv'


def remove_leading_slashes_from_strings(obj):
    twitter_handle = str(obj.twitter_handle)
    match = re.match(r'^/', twitter_handle)
    new_twitter_handle = ""
    if match:
        new_twitter_handle = twitter_handle[1:]
        profile_list = [
            obj.__class__.__name__,
            obj.id,
            twitter_handle,
            new_twitter_handle
        ]
        write_to_csv(profile_list)
        obj.twitter_handle = new_twitter_handle
        obj.save()


def remove_trailing_slashes_from_strings(obj):
    twitter_handle = str(obj.twitter_handle)
    new_twitter_handle = ''
    if twitter_handle.endswith("/"):
        new_twitter_handle = twitter_handle[:-1]
        profile_list = [
            obj.__class__.__name__,
            obj.id,
            twitter_handle,
            new_twitter_handle
        ]
        write_to_csv(profile_list)
        obj.twitter_handle = new_twitter_handle
        obj.save()


def remove_trailing_and_leading_whitespace(obj):
    new_twitter_handle = str(obj.twitter_handle).strip()
    if new_twitter_handle != obj.twitter_handle:
        obj.twitter_handle = new_twitter_handle
        obj.save()


def remove_leading_hastag_on_valid_twitter_handles(Model):

    profiles = Model.objects.filter(twitter_handle__iregex="^#")

    profile_list = profiles.values_list("id", "twitter_handle")
    for profile in profile_list:
        profile = [Model.__name__] + list(profile)
        profile.append(profile[2][1:])
        write_to_csv(profile)

    profiles.update(twitter_handle=Func(
                    F('twitter_handle'),
                    Value("#"),
                    Value(""),
                    function="replace"))


def remove_twitter_url_prefix_from_handles(Model):

    twitter_url_variations = [
        'maapit or https://twitter.com/',
        '@https://twitter.com/',
        'https://twitter.com/#!/',
        'Http://twitter.com/',
        'http://twitter.com/',
        'http://www.twitter.com/',
        'https://mobile.twitter.com/',
        'https://twitter.com/',
        'https://ww.twitter.com/',
        'https://www.Twitter.com/',
        'https://www.twitter.com/',
        'https;//twitter.com/',
        'htttp://www.twitter.com/',
        'www.Twitter.com/',
        'www.twitter.com/',
        'Twitter.com/',
        'twitter.com/',
    ]

    for variation in twitter_url_variations:
        profiles = Model.objects.filter(twitter_handle__startswith=variation)

        profile_list = profiles.values_list("id", "twitter_handle")
        for profile in profile_list:
            profile = [Model.__name__] + list(profile)
            profile.append(profile[2].replace(variation, ""))
            write_to_csv(profile)

        try:
            profiles.update(
                twitter_handle=Func(
                    F('twitter_handle'),
                    Value(variation),
                    Value(""),
                    function="replace"))
        except ValueError as error:
            pass


def remove_not_available_abbreviation_from_twitter_handles(Model):
    profiles = Model.objects.filter(twitter_handle__icontains="n/a")
    create_list_to_write_to_csv(profiles, Model)
    profiles.update(twitter_handle="")


def turn_handles_with_incomplete_handles_to_empty_string(Model):
    profiles = Model.objects.filter(
        twitter_handle="https://twitter.")
    create_list_to_write_to_csv(profiles, Model)
    profiles.update(twitter_handle="")


def remove_hashbang_from_twitter_handles(Model):

    profiles = Model.objects.filter(twitter_handle__iregex="^#!/")

    profile_list = profiles.values_list("id", "twitter_handle")
    for profile in profile_list:
        profile = [Model.__name__] + list(profile)
        profile.append(profile[2][3:])
        write_to_csv(profile)

    profiles.update(twitter_handle=str(F('twitter_handle'))[3:])


def write_to_csv(data_list):
    with open(TWITTER_HANDLE_CSV_FILE_NAME, 'a+') as myfile:
        wr = csv.writer(
            myfile,
            quoting=csv.QUOTE_ALL
        )
        wr.writerow(data_list)


def create_list_to_write_to_csv(profiles, Model, new_handle=""):
    profile_list = profiles.values_list("id", "twitter_handle")
    for profile in profile_list:
        profile = [Model.__name__] + list(profile)
        profile.append(new_handle)
        write_to_csv(profile)
