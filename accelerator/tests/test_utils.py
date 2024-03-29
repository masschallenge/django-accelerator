from mock import patch
from django.test import TestCase

from ..utils import flag_smith_has_feature


class TestUtils(TestCase):
    def test_flag_smith_has_feature(self):
        with patch("flagsmith.Flagsmith.has_feature") as mock_function:
            flag_smith_has_feature("feature_key")
            mock_function.assert_called_with("feature_key")
