# Generated by Django 5.0 on 2023-12-27 17:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_backet"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Backet",
            new_name="Basket",
        ),
    ]
