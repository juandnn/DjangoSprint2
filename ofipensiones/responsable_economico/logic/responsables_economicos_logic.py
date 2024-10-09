from ..models import ResponsableEconomico

def get_responsables_economicos():
    return ResponsableEconomico.objects.all()

def get_responsable_economico_by_cedula(id):
    return ResponsableEconomico.objects.get(id=id)
