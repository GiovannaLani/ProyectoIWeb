# Generated by Django 5.1.2 on 2024-11-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winxAPP', '0003_escuela_directora_escuela_especialidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporada',
            name='sinopsis',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]