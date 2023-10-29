# Generated by Django 4.2.4 on 2023-10-29 14:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viajes', '0024_alter_viaje_general_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje_general',
            name='usuariosPermitidos',
            field=models.ManyToManyField(related_name='viajes', to=settings.AUTH_USER_MODEL),
        ),
    ]
