from mock import patch

from django.test import (
    TestCase,
    override_settings,
)

from accelerator_abstract.models.secure_file_system_storage import (
    SecureFileSystemStorage
)


@override_settings(ROOT_URLCONF='accelerator.tests.urls')
class TestSecureFileSystemStorage(TestCase):

    @patch('accelerator_abstract.models.secure_file_system_storage.settings')
    def test_url_successful_url_reverse(self, mock_settings):
        mock_settings.FILE_PAGE_DOWNLOAD_VIEW = 'mock'
        secure_file_system_storage = SecureFileSystemStorage(location='')
        name = 'bar'
        url = secure_file_system_storage.url(name)
        assert url is not None
        assert name not in url

    @patch('accelerator_abstract.models.secure_file_system_storage.settings')
    def test_url_unsuccessful_url_reverse(self, mock_settings):
        mock_settings.FILE_PAGE_DOWNLOAD_VIEW = 'mock'
        secure_file_system_storage = SecureFileSystemStorage(location='')
        bad_name = 5
        with self.assertRaises(ValueError):
            secure_file_system_storage.url(bad_name)
