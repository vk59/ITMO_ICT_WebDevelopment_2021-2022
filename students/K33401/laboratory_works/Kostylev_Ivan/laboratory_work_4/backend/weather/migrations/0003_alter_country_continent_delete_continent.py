# Generated by Django 4.0.1 on 2022-02-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_user_days_count_alter_continent_continent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[(1, 'Asia'), (2, 'Europe'), (3, 'North America'), (4, 'South America'), (5, 'Oceania'), (6, 'Africa')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Continent',
        ),
    ]