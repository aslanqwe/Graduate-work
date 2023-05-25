from django.contrib import admin
from .models import Articles
from .models import Director
from .models import Clubs

admin.site.register(Articles)
admin.site.register(Director)
admin.site.register(Clubs)