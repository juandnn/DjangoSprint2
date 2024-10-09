from django.shortcuts import render
from .logic import responsables_economicos_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def responsables_economicos_view(request):
    if request.method == 'GET':
        responsable_economicos = vl.get_responsables_economicos()
        responsable_economicos_dto = serializers.serialize('json', responsable_economicos)
    return HttpResponse(responsable_economicos_dto, 'application/json')

