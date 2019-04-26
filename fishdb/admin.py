from django.contrib import admin

from .models import Zebrafish


@admin.register(Zebrafish)
class ZebrafishAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "modified"]
