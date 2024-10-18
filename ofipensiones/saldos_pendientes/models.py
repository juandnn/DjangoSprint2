from django.db import models
from cronogramas_personalizados.models import CronogramaPersonalizado

# Create your models here.
class SaldoPendiente(models.Model):
    id = models.AutoField(primary_key=True)
    valorPendiente = models.IntegerField()
    tipo = models.CharField(max_length=50)
    fechaLimite = models.CharField(max_length=100)
    descuento = models.FloatField()
    interes = models.FloatField()
    estaPagado = models.BooleanField(default=False)
    CronogramaPersonalizado = models.ForeignKey(CronogramaPersonalizado, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
