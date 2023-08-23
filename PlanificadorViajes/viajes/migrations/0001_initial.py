# Generated by Django 4.2.4 on 2023-08-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje_Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDia', models.CharField(max_length=250)),
                ('actividades', models.CharField(max_length=250)),
                ('destinos', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('notas', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje_General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreViaje', models.CharField(max_length=250)),
                ('cantidadDias', models.IntegerField()),
                ('fechaInicio', models.DateField()),
                ('fechaFinalizacion', models.DateField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]
