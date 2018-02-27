# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import base64

from django.conf import settings
from django.core.files.storage import FileSystemStorage

try:
    from django.urls import reverse
except ImportError:  # pragma: no cover - backward compatibility
    from django.core.urlresolvers import reverse  # pragma: no cover


class SecureFileSystemStorage(FileSystemStorage):
    """sucblass that is not accessible via URL

    files stored using this storage will not be accessible via any url, they
    must be accessed using a view that provides direct access to the file
    bytes as a response.
    """

    def __init__(self, location=None):
        super(SecureFileSystemStorage, self).__init__(location)
        self.base_url = None

    def url(self, name):
        """provide a download url for site staff/admins only
        security is enforced by the endpoint of the url, not by this method
        this method is provided to ensure that admin pages can show this file
        as uploaded.
        """
        try:
            if isinstance(name, str):
                name = name.encode('utf-8')
            encoded_name = base64.urlsafe_b64encode(name)
            url = reverse(settings.FILE_PAGE_DOWNLOAD_VIEW,
                          args=(encoded_name,))
        except TypeError:
            raise ValueError("This file is not accessible via a URL.")
        return url
