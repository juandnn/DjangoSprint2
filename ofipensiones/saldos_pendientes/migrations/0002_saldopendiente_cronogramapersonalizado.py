# Generated by Django 3.2.6 on 2024-10-18 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cronogramas_personalizados', '0002_remove_cronogramapersonalizado_saldo_pendiente'),
        ('saldos_pendientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saldopendiente',
            name='CronogramaPersonalizado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cronogramas_personalizados.cronogramapersonalizado'),
            preserve_default=False,
        ),
    ]