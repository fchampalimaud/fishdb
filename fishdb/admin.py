from django.contrib import admin

from .models import Fish
from .models import Species
from .models import Category
from .models import Location

admin.site.register(Fish)
admin.site.register(Species)
admin.site.register(Category)
admin.site.register(Location)
