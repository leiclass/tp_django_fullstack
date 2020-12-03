# Generated by Django 3.1.3 on 2020-12-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20201130_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historia',
            name='paciente',
        ),
        migrations.AddField(
            model_name='historia',
            name='paciente',
            field=models.ManyToManyField(related_name='historias', to='pacientes.Paciente'),
        ),
    ]