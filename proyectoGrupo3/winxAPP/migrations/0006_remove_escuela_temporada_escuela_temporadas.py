# Generated by Django 5.1.2 on 2024-11-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winxAPP', '0005_temporada_numerotemporada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escuela',
            name='temporada',
        ),
        migrations.AddField(
            model_name='escuela',
            name='temporadas',
            field=models.ManyToManyField(related_name='escuelas', to='winxAPP.temporada'),
        ),
    ]
