# Generated by Django 4.2.4 on 2023-08-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SitioWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(),
        ),
    ]