# Generated by Django 3.2 on 2022-10-20 17:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_auto_20221019_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileModel',
            new_name='Profile',
        ),
    ]
