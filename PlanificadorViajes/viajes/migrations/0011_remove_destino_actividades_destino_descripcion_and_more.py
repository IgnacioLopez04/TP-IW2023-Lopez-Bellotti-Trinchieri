# Generated by Django 4.2.4 on 2023-08-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0010_alter_viaje_general_diasviaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='actividades',
        ),
        migrations.AddField(
            model_name='destino',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Actividad',
        ),
    ]