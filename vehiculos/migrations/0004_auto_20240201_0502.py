# Generated by Django 3.2.13 on 2024-02-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_auto_20230705_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='serial_carroceria',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='serial_motor',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='condicion',
            field=models.CharField(choices=[['Nuevo', 'Nuevo'], ['Seminuevo', 'Seminuevo'], ['Usado', 'Usado']], default='Nuevo', max_length=50),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
    ]
