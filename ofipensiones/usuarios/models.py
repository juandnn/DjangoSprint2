from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cedula + self.nombre