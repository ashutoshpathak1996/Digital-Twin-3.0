# Generated by Django 4.0.2 on 2022-03-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twinregister', '0002_alter_verticlemilling_floor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='verticlemilling',
            name='otherdetails_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
