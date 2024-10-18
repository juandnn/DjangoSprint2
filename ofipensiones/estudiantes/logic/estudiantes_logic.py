from .. import models
from cronogramas_personalizados.models import CronogramaPersonalizado

def get_estudiantes():
    return models.Estudiantes.objects.all()

def get_estudiante_by_id(id):
    return models.Estudiantes.objects.get(id=id)

def update_estudiante(id, new_var):
    estudiante = models.Estudiantes.objects.get(id=id)
    estudiante.nombre = new_var['nombre']
    estudiante.curso = new_var['curso']

    cronograma = CronogramaPersonalizado.objects.get(id=new_var['cronograma_personalizado'])
    estudiante.cronograma_personalizado = cronograma

    estudiante.save()
    return estudiante

