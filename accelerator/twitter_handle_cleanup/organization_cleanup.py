import re


def clean_organization_twitter_handles(Organization):
    # remove leading twitter.com/ from handles
    orgs = Organization.objects.filter(
        twitter_handle__contains="twitter.com/")
    for org in orgs:
        old = org.twitter_handle
        new = org.twitter_handle[org.twitter_handle.index('twitter.com/')+12:]
        org.twitter_handle = new
        org.save()
        print(org.name, old, new)

    # remove leading Twitter.com/ from handles
    orgs = Organization.objects.filter(
        twitter_handle__contains="Twitter.com/")
    for org in orgs:
        old = org.twitter_handle
        new = org.twitter_handle[org.twitter_handle.index('Twitter.com/')+12:]
        org.twitter_handle = new
        org.save()
        print(org.name, old, new)

    # remove 'n/a' from handles
    for org in Organization.objects.filter(twitter_handle__icontains="n/a"):
        insensitive_na = re.compile(re.escape('n/a'), re.IGNORECASE)
        new = insensitive_na.sub('', org.twitter_handle)
        old = org.twitter_handle
        org.twitter_handle = new
        org.save()
        print(org.name, old, new)

    for org in Organization.objects.exclude(twitter_handle=""):
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
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
                print(org.name, old_handle, new_handle)

        # remove trailing and leading whitespace
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
        if not match:
            old = org.twitter_handle
            new = org.twitter_handle.strip()
            org.twitter_handle = new
            org.save()

        # remove leading hashtag on valid twitter handles
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
        if not match:
            match = re.search(r'#(@?(\w){1,15})', org.twitter_handle)
            if match:
                old_handle = org.twitter_handle
                new_handle = org.twitter_handle[1:]
                org.twitter_handle = new_handle
                org.save()
                print(org.name, old_handle, new_handle)

        # remove trailing slashes from strings
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
        if not match:
            match = re.search(r'/$', org.twitter_handle)
            if match:
                old = org.twitter_handle
                new = org.twitter_handle[:-1]
                org.twitter_handle = new
                org.save()
                print(org.name, old, new)

        # remove leading slashes from strings
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
        if not match:
            match = re.search(r'^/', org.twitter_handle)
            if match:
                old = org.twitter_handle
                new = org.twitter_handle[1:]
                org.twitter_handle = new
                org.save()
                print(org.name, old, new)

        # remove leading hashbang situation
        match = re.match(r'^@?(\w){1,15}$', org.twitter_handle)
        if not match:
            match = re.search(r'^#!/', org.twitter_handle)
            if match:
                old = org.twitter_handle
                new = org.twitter_handle[3:]
                org.twitter_handle = new
                org.save()
                print(org.name, old, new)
