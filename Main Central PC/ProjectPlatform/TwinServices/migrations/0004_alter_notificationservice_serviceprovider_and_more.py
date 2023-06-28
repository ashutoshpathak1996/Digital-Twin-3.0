# Generated by Django 4.0.2 on 2022-05-28 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TwinServices', '0003_services_provider_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationservice',
            name='serviceprovider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Services_provider',
        ),
    ]