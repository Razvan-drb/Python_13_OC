from django.test import TestCase
from lettings.apps import LettingsConfig


class LettingsAppConfigTest(TestCase):
    """Test suite for Lettings app config."""

    def test_lettings_app_config(self):
        """Test that the app config is correctly set up."""
        self.assertEqual(LettingsConfig.name, 'lettings')
