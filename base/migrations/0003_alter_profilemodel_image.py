# Generated by Django 3.2 on 2022-10-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221019_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(blank=True, default='/user.png', height_field='100', null=True, upload_to='images', width_field='100'),
        ),
    ]