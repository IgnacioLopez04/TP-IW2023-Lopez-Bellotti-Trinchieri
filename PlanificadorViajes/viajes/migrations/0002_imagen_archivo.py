# Generated by Django 4.2.4 on 2023-08-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen_Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('image_data', models.BinaryField(null=True)),
            ],
        ),
    ]
