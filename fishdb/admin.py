from django.contrib import admin

from . import models


@admin.register(models.Fish)
class FishAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "modified"]


admin.site.register(models.Species)
admin.site.register(models.Category)
admin.site.register(models.Location)
