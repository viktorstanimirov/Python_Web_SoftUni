# Generated by Django 5.0.2 on 2024-02-27 11:01

import world_of_speed_app.profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(help_text='Age requirement: 21 years and above.', validators=[world_of_speed_app.profiles.validators.validate_age]),
        ),
    ]