# Generated by Django 4.0.1 on 2022-01-28 09:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0003_conference_members_delete_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='members',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
