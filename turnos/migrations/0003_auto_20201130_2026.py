# Generated by Django 3.1.3 on 2020-11-30 20:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_turno_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 30, 20, 26, 56, 842240, tzinfo=utc)),
        ),
    ]