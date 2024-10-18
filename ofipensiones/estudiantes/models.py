from django.db import models
from saldos_pendientes.models import SaldoPendiente
from cronogramas_personalizados.models import CronogramaPersonalizado



# Create your models here.
class Estudiantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    curso = models.CharField(max_length=100)
    cronograma_personalizado = models.OneToOneField(CronogramaPersonalizado, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre
