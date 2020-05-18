from django.conf import settings
from django.db import migrations


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authnapp.models import ShopUser

            ShopUser.objects.create_superuser("Admin", "SuroviyDron@google.com", "123", age=27)

        except:

            print("Cann't create super user for debug")


def reverse_func(apps, schema_editor):
    if settings.DEBUG:

        try:
            from authnapp.models import ShopUser

            ShopUser.objects.create_superuser("Admin", "SuroviyDron@google.com", "123", age=27)

        except:
            print("Cann't delete super user for debug")


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
