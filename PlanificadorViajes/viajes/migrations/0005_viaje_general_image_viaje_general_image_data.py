# Generated by Django 4.2.4 on 2023-08-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0004_remove_viaje_general_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje_general',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='viaje_general',
            name='image_data',
            field=models.BinaryField(null=True),
        ),
    ]