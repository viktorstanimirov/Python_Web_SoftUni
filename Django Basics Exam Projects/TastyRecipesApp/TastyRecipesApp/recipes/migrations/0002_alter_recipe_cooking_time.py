# Generated by Django 5.0.4 on 2024-04-17 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(help_text='Provide the cooking time in minutes.', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]