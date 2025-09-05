from django.db import migrations

def forwards_func_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old_obj in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_obj.id,
            user=old_obj.user,
            favorite_city=old_obj.favorite_city
        )

def reverse_func_profiles(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func_profiles, reverse_func_profiles),
    ]