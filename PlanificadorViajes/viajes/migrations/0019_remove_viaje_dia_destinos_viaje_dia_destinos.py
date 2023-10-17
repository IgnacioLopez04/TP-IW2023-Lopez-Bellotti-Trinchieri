# Generated by Django 4.2.4 on 2023-10-17 18:31

from django.db import migrations, models
import viajes.models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0018_viaje_general_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viaje_dia',
            name='destinos',
        ),
        migrations.AddField(
            model_name='viaje_dia',
            name='destinos',
            field=models.JSONField(null=True, verbose_name=viajes.models.Destino),
        ),
    ]