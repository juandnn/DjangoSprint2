# Generated by Django 3.2.6 on 2024-10-18 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronogramas_personalizados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronogramapersonalizado',
            name='saldo_pendiente',
        ),
    ]