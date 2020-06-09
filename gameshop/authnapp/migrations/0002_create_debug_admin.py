from django.conf import settings
from django.db import migrations, transaction


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authnapp.models import ShopUser

            with transaction.atomic():
                ShopUser.objects.create_superuser("admin", "root@google.com", "admin", age=33)
        except Exception as exp:
            print(f"Cann't create super user for debug: {exp}")


def reverse_func(apps, schema_editor):
    if settings.DEBUG:
        try:
            from authnapp.models import ShopUser

            with transaction.atomic():
                ShopUser.objects.all().delete()
        except Exception as exp:
            print(f"Cann't delete super user for debug: {exp}")


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
