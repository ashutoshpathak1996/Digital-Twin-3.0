# Generated by Django 4.0.2 on 2022-06-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twinregister', '0006_rename_is_loaded_verticlemilling_coolant_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='verticlemilling',
            name='spindle_speed',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
