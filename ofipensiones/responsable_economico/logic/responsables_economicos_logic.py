from ..models import ResponsableEconomico

def get_responsables_economicos():
    return ResponsableEconomico.objects.all()

