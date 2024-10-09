from django.shortcuts import render
from .logic import usuarios_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def usuarios_view(request, username=None):
    if request.method == 'GET':
        if username:
            try:
                usuario_dto = vl.get_usuario_by_username(username)
                usuario = serializers.serialize('json', [usuario_dto])
                return HttpResponse(usuario, 'application/json')
            except vl.models.Usuario.DoesNotExist:
                return HttpResponse(json.dumps({'error': 'Usuario no encontrado'}), 'application/json', status=404)
        else:
            usuarios_dto = vl.get_usuarios()
            usuarios = serializers.serialize('json', usuarios_dto)
            return HttpResponse(usuarios, 'application/json')
    
    if request.method == 'POST':
        usuario_dto = vl.update_usuario(username, json.loads(request.body.decode('utf-8')))
        usuario = serializers.serialize('json', [usuario_dto])
        return HttpResponse(usuario, 'application/json')
