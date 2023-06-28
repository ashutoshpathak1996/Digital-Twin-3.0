# Generated by Django 4.0.2 on 2022-06-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TwinServices', '0005_remove_notificationservice_twin_selected_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationservice',
            name='services',
        ),
        migrations.AddField(
            model_name='notificationservice',
            name='services',
            field=models.ManyToManyField(to='TwinServices.Services_Outsourced'),
        ),
    ]
