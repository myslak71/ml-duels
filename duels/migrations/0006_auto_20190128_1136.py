# Generated by Django 2.1.1 on 2019-01-28 11:36

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duels', '0005_auto_20190128_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duel',
            name='user1_percentage',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=6, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]), default=list, null=True, size=3),
        ),
        migrations.AlterField(
            model_name='duel',
            name='user2_percentage',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=6, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]), default=list, null=True, size=3),
        ),
    ]