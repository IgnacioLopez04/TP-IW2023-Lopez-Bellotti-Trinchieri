# Generated by Django 4.2.4 on 2023-08-29 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0005_viaje_general_image_viaje_general_image_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viaje_general',
            name='fechaFinalizacion',
        ),
        migrations.RemoveField(
            model_name='viaje_general',
            name='fechaInicio',
        ),
    ]
