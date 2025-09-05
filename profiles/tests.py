from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    """Test suite for the Profile model."""

    def test_profile_creation(self):
        """Test that a Profile can be created."""
        user = User.objects.create_user(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user, favorite_city="Test City")
        self.assertEqual(profile.user.username, "testuser")
        self.assertEqual(profile.favorite_city, "Test City")


class ProfileViewTest(TestCase):
    """Test suite for Profile views."""

    def setUp(self):
        """Set up data for the tests."""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profiles_index_view(self):
        """Test that the profiles index view returns a 200 response."""
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    def test_profile_detail_view(self):
        """Test that the profile detail view returns a 200 response."""
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
