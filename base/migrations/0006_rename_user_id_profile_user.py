# Generated by Django 3.2 on 2022-10-21 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_profilemodel_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]