import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()

from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


def create_users_and_profiles():
    """Crée les users et profiles originaux."""
    users_data = [
        {'username': '4meRomance', 'email': 'coemperor@famemma.net', 'first_name': 'John', 'last_name': 'Rodriguez',
         'favorite_city': 'Chicago'},
        {'username': 'AirWow', 'email': 'flocation.vam4@glendenningflowerdesign.com', 'first_name': 'Ada',
         'last_name': 'Paul', 'favorite_city': 'New York'},
        {'username': 'DavWin', 'email': '5houssam.kessaiso@facpidif.ml', 'first_name': 'Cassandra',
         'last_name': 'Grahm', 'favorite_city': 'Miami'},
        {'username': 'HeadlinesGazer', 'email': 'jssssss33@acee9.live', 'first_name': 'Jamie', 'last_name': 'Lal',
         'favorite_city': 'Las Vegas'}
    ]

    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name']
            }
        )
        Profile.objects.get_or_create(
            user=user,
            defaults={'favorite_city': user_data['favorite_city']}
        )
    print("Users and Profiles created!")


def create_addresses_and_lettings():
    """Crée les addresses et lettings originaux."""
    addresses_data = [
        {'number': 7217, 'street': "Bedford Street", 'city': "Brunswick", 'state': "GA", 'zip_code': 31525,
         'country_iso_code': "USA"},
        {'number': 4, 'street': "Military Street", 'city': "Willoughby", 'state': "OH", 'zip_code': 44094,
         'country_iso_code': "USA"},
        {'number': 34057, 'street': "Glendale Street", 'city': "Fremont", 'state': "CA", 'zip_code': 94536,
         'country_iso_code': "USA"},
        {'number': 7930, 'street': "Marsh Street", 'city': "Westmont", 'state': "IL", 'zip_code': 60559,
         'country_iso_code': "USA"},
        {'number': 83, 'street': "West Street", 'city': "Fitchburg", 'state': "MA", 'zip_code': 1420,
         'country_iso_code': "USA"},
        {'number': 115, 'street': "Cedar Street", 'city': "Longview", 'state': "TX", 'zip_code': 75604,
         'country_iso_code': "USA"}
    ]

    lettings_titles = [
        "Joshua Tree Green Haus /w Hot Tub",
        "Oceanview Retreat",
        "'Silo Studio' Cottage",
        "Pirates of the Caribbean Getaway",
        "The Mushroom Dome Retreat & LAND of Paradise Suite",
        "Underground Hygge"
    ]

    # Création des addresses
    addresses = []
    for addr_data in addresses_data:
        address, created = Address.objects.get_or_create(**addr_data)
        addresses.append(address)

    # Création des lettings
    for i, title in enumerate(lettings_titles):
        Letting.objects.get_or_create(title=title, address=addresses[i])

    print("Addresses and Lettings created!")


if __name__ == '__main__':
    # Vide la base existante pour repartir de zéro
    Profile.objects.all().delete()
    Letting.objects.all().delete()
    Address.objects.all().delete()
    User.objects.exclude(username='admin').delete()  # Garde le superuser admin

    # Crée toutes les données
    create_users_and_profiles()
    create_addresses_and_lettings()

    print("Database populated successfully!")
    print(f"Total Users: {User.objects.count()}")
    print(f"Total Profiles: {Profile.objects.count()}")
    print(f"Total Addresses: {Address.objects.count()}")
    print(f"Total Lettings: {Letting.objects.count()}")
