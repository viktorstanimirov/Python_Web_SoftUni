# Generated by Django 4.2.4 on 2024-02-28 09:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('POP', 'Pop Music'), ('JAZZ', 'Jazz Music'), ('R_AND_B', 'R&B Music'), ('ROCK', 'Rock Music'), ('COUNTRY', 'Country Music'), ('DANCE', 'Dance Music'), ('HIP_HOP', 'Hip Hop Music'), ('OTHER', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]