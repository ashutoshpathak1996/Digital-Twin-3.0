# Generated by Django 4.0.2 on 2022-05-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_is_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_serviceprovider',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
