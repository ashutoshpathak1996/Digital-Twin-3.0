# Generated by Django 4.0.2 on 2022-03-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_is_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_manufacturer',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
