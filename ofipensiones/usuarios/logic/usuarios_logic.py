from .. import models

def get_usuarios():
    return models.Usuario.objects.all()

def get_usuario_by_username(username):
    return models.Usuario.objects.get(username=username)

def update_usuario(username, new_var):
    usuario = get_usuario_by_username(username)
    usuario.username = new_var['username']
    usuario.clave = new_var['clave']
    usuario.save()
    return usuario

