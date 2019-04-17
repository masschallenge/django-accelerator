import re


def clean_entrepreneur_profile_twitter_handles(EntrepreneurProfile):
    # remove leading twitter.com/ from handles
    profiles = EntrepreneurProfile.objects.filter(
        twitter_handle__contains="twitter.com/")
    for ent in profiles:
        old = ent.twitter_handle
        new = ent.twitter_handle[ent.twitter_handle.index('twitter.com/')+12:]
        ent.twitter_handle = new
        ent.save()
        print(ent, old, new)

    # empty "https://twitter." from handles
    profiles = EntrepreneurProfile.objects.filter(
        twitter_handle="https://twitter.")
    for ent in profiles:
        old = ent.twitter_handle
        new = ""
        ent.twitter_handle = new
        ent.save()
        print(ent, old, new)

    # remove 'n/a' from handles
    profiles = EntrepreneurProfile.objects.filter(
        twitter_handle__icontains="n/a")
    for ent in profiles:
        insensitive_na = re.compile(re.escape('n/a'), re.IGNORECASE)
        new = insensitive_na.sub('', ent.twitter_handle)
        old = ent.twitter_handle
        ent.twitter_handle = new
        ent.save()
        print(ent, old, new)

    for ent in EntrepreneurProfile.objects.exclude(twitter_handle=""):
        # remove trailing and leading whitespace
        match = re.match(r'^@?(\w){1,15}$', ent.twitter_handle)
        if not match:
            old = ent.twitter_handle
            new = ent.twitter_handle.strip()
            ent.twitter_handle = new
            ent.save()

        # remove leading hashtag on valid twitter handles
        match = re.match(r'^@?(\w){1,15}$', ent.twitter_handle)
        if not match:
            match = re.search(r'#(@?(\w){1,15})', ent.twitter_handle)
            if match:
                old_handle = ent.twitter_handle
                new_handle = ent.twitter_handle[1:]
                ent.twitter_handle = new_handle
                ent.save()
                print(ent, old_handle, new_handle)

        # remove trailing slashes from strings
        match = re.match(r'^@?(\w){1,15}$', ent.twitter_handle)
        if not match:
            match = re.search(r'/$', ent.twitter_handle)
            if match:
                old = ent.twitter_handle
                new = ent.twitter_handle[:-1]
                ent.twitter_handle = new
                ent.save()
                print(ent, old, new)

        # remove leading slashes from strings
        match = re.match(r'^@?(\w){1,15}$', ent.twitter_handle)
        if not match:
            match = re.search(r'^/', ent.twitter_handle)
            if match:
                old = ent.twitter_handle
                new = ent.twitter_handle[1:]
                ent.twitter_handle = new
                ent.save()
                print(ent, old, new)
