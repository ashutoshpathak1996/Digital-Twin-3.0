# Generated by Django 4.0.2 on 2022-06-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TwinServices', '0011_alter_notificationservice_services'),
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
