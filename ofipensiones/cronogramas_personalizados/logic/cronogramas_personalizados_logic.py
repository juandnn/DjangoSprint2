from .. import models

def get_usuarios():
    return models.CronogramaPersonalizado.objects.all()

def get_usuario_by_username(id):
    return models.CronogramaPersonalizado.objects.get(id=id)