# Generated by Django 3.2 on 2022-10-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_profilemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to='images'),
        ),
    ]