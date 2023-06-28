# Generated by Django 4.0.2 on 2022-06-01 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TwinServices', '0006_remove_notificationservice_services_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceprovider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceprovider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='notificationservice',
            name='serviceprovider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sp', to='TwinServices.serviceprovider'),
        ),
    ]