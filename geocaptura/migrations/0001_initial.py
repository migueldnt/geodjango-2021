# Generated by Django 3.2.8 on 2021-10-09 05:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ubicacion', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('descripcion', models.TextField(default='')),
                ('tipo', models.CharField(choices=[('bache', 'Bache'), ('falta_alumbrado', 'Falta de alumbrado'), ('semaforo', 'Falla de semaforo'), ('otros', 'Otros')], default='normal', max_length=20)),
                ('status', models.CharField(choices=[('pendiente', 'pendiente'), ('resuelto', 'resuelto'), ('en_proceso', 'en_proceso')], default='pendiente', max_length=20)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
