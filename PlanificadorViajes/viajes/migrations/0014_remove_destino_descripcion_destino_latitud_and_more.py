# Generated by Django 4.2.4 on 2023-09-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0013_alter_viaje_general_calificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='destino',
            name='latitud',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='destino',
            name='longitud',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='destino',
            name='provincia',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
