# Generated by Django 4.0.2 on 2022-02-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_manufacturer',
            field=models.BooleanField(default=False),
        ),
    ]
