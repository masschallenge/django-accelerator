from django.test import TestCase
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from accelerator_abstract.models.secure_file_system_storage import (
    SecureFileSystemStorage
)


class TestSecureFileSystemStorage(TestCase):

    @patch('accelerator_abstract.models.secure_file_system_storage.settings')
    def test_url_successful_url_reverse(self, mock_settings):
        mock_settings.FILE_PAGE_DOWNLOAD_VIEW = 'mock'
        secure_file_system_storage = SecureFileSystemStorage(location='')
        name = 'bar'
        url = secure_file_system_storage.url(name)
        assert url is not None

    @patch('accelerator_abstract.models.secure_file_system_storage.settings')
    def test_url_unsuccessful_url_reverse(self, mock_settings):
        mock_settings.FILE_PAGE_DOWNLOAD_VIEW = 'mock'
        secure_file_system_storage = SecureFileSystemStorage(location='')
        bad_name = 5
        with self.assertRaises(ValueError):
            secure_file_system_storage.url(bad_name)
