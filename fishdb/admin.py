from django.contrib import admin

from .models import Fish
from .models import Species

admin.site.register(Fish)
admin.site.register(Species)
