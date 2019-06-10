from django.contrib import admin

from .models import Fish
from .models import Species
from .models import Category

admin.site.register(Fish)
admin.site.register(Species)
admin.site.register(Category)
