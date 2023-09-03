# Generated by Django 4.0.1 on 2023-08-13 03:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_credentials',
            name='csv',
            field=models.FileField(blank=True, null=True, upload_to='personal_files/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
