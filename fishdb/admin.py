from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ExportActionMixin, ImportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from . import models
from .models import Fish, Category, Species


class FishResource(resources.ModelResource):
    category = Field(attribute='category', column_name='category', widget=ForeignKeyWidget(Category, 'name'))
    species = Field(attribute='species', column_name='species', widget=ForeignKeyWidget(Species, 'name'))
    class Meta:
        model = Fish
        skip_unchanged = True
        report_skipped = True
        clean_model_instances = True

class FishAdmin(ImportMixin, ExportActionMixin, admin.ModelAdmin):
    resource_class = FishResource
    readonly_fields = ["created", "modified"]

admin.site.register(Fish, FishAdmin)
admin.site.register(models.Species)
admin.site.register(models.Category)
admin.site.register(models.Location)
