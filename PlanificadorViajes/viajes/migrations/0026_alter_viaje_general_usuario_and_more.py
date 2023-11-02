# Generated by Django 4.2.4 on 2023-10-29 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viajes', '0025_alter_viaje_general_usuariospermitidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje_general',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='viaje_general',
            name='usuariosPermitidos',
            field=models.ManyToManyField(blank=True, related_name='viajes', to=settings.AUTH_USER_MODEL),
        ),
    ]