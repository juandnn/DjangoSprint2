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
                usuario = vl.get_usuario_by_username(username)
                usuario_dto = serializers.serialize('json', [usuario])
                return HttpResponse(usuario_dto, 'application/json')
            except vl.models.Usuario.DoesNotExist:
                return HttpResponse(json.dumps({'error': 'Usuario no encontrado'}), 'application/json', status=404)
        else:
            usuarios = vl.get_usuarios()
            usuarios_dto = serializers.serialize('json', usuarios)
            return HttpResponse(usuarios_dto, 'application/json')