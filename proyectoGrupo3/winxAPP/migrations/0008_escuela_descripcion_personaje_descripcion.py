# Generated by Django 5.1.2 on 2024-11-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winxAPP', '0007_personaje_genero_personaje_origen'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='descripcion',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='personaje',
            name='descripcion',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
