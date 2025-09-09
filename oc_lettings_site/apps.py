from django.apps import AppConfig
from django.db.models.signals import post_migrate


def load_initial_data(sender, **kwargs):
    """Load initial data after migrations complete"""
    from django.core.management import call_command

    # Check if data already exists to avoid duplicates
    from lettings.models import Letting
    from profiles.models import Profile

    if not Letting.objects.exists() and not Profile.objects.exists():
        print("Loading initial data from fixtures...")
        call_command('loaddata', 'users.json')
        call_command('loaddata', 'lettings.json')
        call_command('loaddata', 'profiles.json')


class OCLettingsSiteConfig(AppConfig):
    name = 'oc_lettings_site'

    def ready(self):
        # Connect the signal to load data after migrations
        post_migrate.connect(load_initial_data, sender=self)
