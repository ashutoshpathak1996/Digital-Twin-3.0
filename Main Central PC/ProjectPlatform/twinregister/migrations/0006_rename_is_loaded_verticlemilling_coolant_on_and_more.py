# Generated by Django 4.0.2 on 2022-06-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twinregister', '0005_alter_verticlemilling_coolant_aas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verticlemilling',
            old_name='is_loaded',
            new_name='coolant_on',
        ),
        migrations.RenameField(
            model_name='verticlemilling',
            old_name='power_on',
            new_name='spindle_on',
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='axis_pos_x',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='axis_pos_y',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='axis_pos_z',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='feed_x',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='feed_y',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='feed_z',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verticlemilling',
            name='job_file_name',
            field=models.CharField(default='none', max_length=300),
            preserve_default=False,
        ),
    ]
