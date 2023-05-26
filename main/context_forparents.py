from .models import ForParents

def forparents(request):
    return {'roditeli': ForParents.objects.all()}
