from django.test import TestCase
from django.urls import reverse


class OcLettingsSiteTest(TestCase):
    """Test suite for the main site."""

    def test_index_view(self):
        """Test that the index view returns a 200 response."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Holiday Homes")

    def test_404_view(self):
        """Test that the custom 404 view works."""
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page not found", status_code=404)
