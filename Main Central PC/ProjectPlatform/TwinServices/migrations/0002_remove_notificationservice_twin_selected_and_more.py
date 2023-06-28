# Generated by Django 4.0.2 on 2022-05-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twinregister', '0005_alter_verticlemilling_coolant_aas_and_more'),
        ('TwinServices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationservice',
            name='twin_selected',
        ),
        migrations.AddField(
            model_name='notificationservice',
            name='twin_selected',
            field=models.ManyToManyField(to='twinregister.VerticleMilling'),
        ),
    ]
