# Generated by Django 5.0.2 on 2024-03-17 12:20

import MyPlant_App.profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('OUTDOOR', 'Outdoor Plants'), ('INDOOR', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[MyPlant_App.profiles.validators.validate_plant_name])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
