from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingModelTest(TestCase):
    """Test suite for the Letting model."""

    def test_letting_creation(self):
        """Test that a Letting can be created."""
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(title="Test Letting", address=address)
        self.assertEqual(letting.title, "Test Letting")
        self.assertEqual(letting.address, address)

    def test_address_str_method(self):
        """Test the Address model's __str__ method."""
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA"
        )
        self.assertEqual(str(address), "123 Main St")

    def test_letting_str_method(self):
        """Test the Letting model's __str__ method."""
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(title="Test Letting", address=address)
        self.assertEqual(str(letting), "Test Letting")


class LettingViewTest(TestCase):
    """Test suite for Letting views."""

    def setUp(self):
        """Set up data for the tests."""
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index_view(self):
        """Test that the lettings index view returns a 200 response."""
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    def test_letting_detail_view(self):
        """Test that the letting detail view returns a 200 response."""
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    def test_letting_detail_view_not_found(self):
        """Test that the letting detail view returns a 404 for non-existent letting."""
        response = self.client.get(reverse('lettings:letting', args=[999]))
        self.assertEqual(response.status_code, 404)
