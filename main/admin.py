from django.contrib import admin
from .models import Articles
from .models import Director
from .models import Clubs
from .models import ForParents
from .models import About
admin.site.register(Articles)
admin.site.register(Director)
admin.site.register(Clubs)
admin.site.register(ForParents)
admin.site.register(About)