from django.apps import AppConfig
from django.db.models.signals import post_migrate


def load_initial_data(sender, **kwargs):
    """Load initial data after migrations complete"""
    from django.core.management import call_command
    from lettings.models import Letting
    from profiles.models import Profile

    print("DEBUG: post_migrate signal received!")  # Debug line

    if not Letting.objects.exists() and not Profile.objects.exists():
        print("DEBUG: Loading initial data from fixtures...")
        call_command('loaddata', 'users.json')
        call_command('loaddata', 'lettings.json')
        call_command('loaddata', 'profiles.json')
    else:
        print("DEBUG: Data already exists, skipping fixture loading")


class OCLettingsSiteConfig(AppConfig):
    name = 'oc_lettings_site'

    def ready(self):
        print("DEBUG: AppConfig ready() method called")  # Debug line
        post_migrate.connect(load_initial_data, sender=self)