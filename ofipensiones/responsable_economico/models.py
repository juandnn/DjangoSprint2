from django.db import models
# Create your models here.
from usuarios.models import Usuario

class ResponsableEconomico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    moroso = models.BooleanField(default=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.cedula + self.nombre
