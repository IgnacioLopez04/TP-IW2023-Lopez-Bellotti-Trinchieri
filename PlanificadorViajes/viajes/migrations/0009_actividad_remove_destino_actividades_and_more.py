# Generated by Django 4.2.4 on 2023-08-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0008_viaje_general_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='destino',
            name='actividades',
        ),
        migrations.AddField(
            model_name='destino',
            name='actividades',
            field=models.ManyToManyField(related_name='destino', to='viajes.actividad'),
        ),
    ]