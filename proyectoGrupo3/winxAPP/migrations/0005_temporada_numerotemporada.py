# Generated by Django 5.1.2 on 2024-11-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winxAPP', '0004_alter_temporada_sinopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporada',
            name='numeroTemporada',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
