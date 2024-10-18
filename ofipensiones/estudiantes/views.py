from django.shortcuts import render
from .logic import estudiantes_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def estudiantes_view(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                estudiante_dto = vl.get_estudiante_by_id(id)
                estudiante = serializers.serialize('json', [estudiante_dto])
                return HttpResponse(estudiante, 'application/json')
            except vl.models.Estudiantes.DoesNotExist:
                return HttpResponse(json.dumps({'error': 'Estudiante no encontrado'}), 'application/json', status=404)
        else:
            estudiantes_dto = vl.get_estudiantes()
            estudiantes = serializers.serialize('json', estudiantes_dto)
            return HttpResponse(estudiantes, 'application/json')
    
    if request.method == 'POST':
        estudiante_dto = vl.update_estudiante(id, json.loads(request.body.decode('utf-8')))
        estudiante = serializers.serialize('json', [estudiante_dto])
        return HttpResponse(estudiante, 'application/json')
