# Generated by Django 4.0.1 on 2022-01-28 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0002_remove_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
