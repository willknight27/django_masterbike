# Generated by Django 3.2.3 on 2021-06-21 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bicicleta_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arriendo',
            name='fecha_inicio',
        ),
        migrations.RemoveField(
            model_name='arriendo',
            name='fecha_termino',
        ),
    ]