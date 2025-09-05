from django.db import migrations


# 1. Import des modèles de l'ANCIENNE application
def forwards_func_lettings(apps, schema_editor):
    # On récupère les modèles de l'ancienne app
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    # On récupère les modèles de la NOUVELLE app
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Pour chaque ancien objet Address, on crée un nouvel objet Address
    for old_obj in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_obj.id,
            number=old_obj.number,
            street=old_obj.street,
            city=old_obj.city,
            state=old_obj.state,
            zip_code=old_obj.zip_code,
            country_iso_code=old_obj.country_iso_code
        )

    # Pour chaque ancien objet Letting, on crée un nouvel objet Letting
    # Note: la clé étrangère 'address' pointe maintenant vers le nouvel objet Address
    for old_obj in OldLetting.objects.all():
        new_address = NewAddress.objects.get(id=old_obj.address.id)
        NewLetting.objects.create(
            id=old_obj.id,
            title=old_obj.title,
            address=new_address
        )

# 2. Fonction pour revenir en arrière (reverse migration) - souvent laissée vide
def reverse_func_lettings(apps, schema_editor):
    # On pourrait supprimer les données des nouvelles tables ici,
    # mais pour une migration de données, c'est souvent complexe à inverser.
    # On laisse souvent cette fonction vide par sécurité.
    pass

class Migration(migrations.Migration):

    dependencies = [
        # Cette migration dépend de la migration initiale de 'lettings'
        # et de l'état actuel de 'oc_lettings_site'
        ('lettings', '0001_initial'),
    ]

    operations = [
        # L'opération RunPython qui exécute notre code de copie
        migrations.RunPython(forwards_func_lettings, reverse_func_lettings),
    ]