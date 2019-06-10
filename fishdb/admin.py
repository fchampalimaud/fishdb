from django.contrib import admin

from .models import Fish
from .models import Species
from .models import Line

admin.site.register(Fish)
admin.site.register(Species)
admin.site.register(Line)
