# Generated by Django 3.1.3 on 2020-11-30 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 30, 20, 23, 42, 655079)),
        ),
    ]
