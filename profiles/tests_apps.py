from django.test import TestCase
from profiles.apps import ProfilesConfig


class ProfilesAppConfigTest(TestCase):
    """Test suite for Profiles app config."""

    def test_profiles_app_config(self):
        """Test that the app config is correctly set up."""
        self.assertEqual(ProfilesConfig.name, 'profiles')
