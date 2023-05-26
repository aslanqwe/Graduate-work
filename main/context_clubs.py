from .models import Clubs

def krujki(request):
    return {'krujki': Clubs.objects.all()}
