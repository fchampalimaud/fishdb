from django.contrib import admin
from django.conf import settings
from import_export import resources, widgets
from import_export.admin import ExportActionMixin, ImportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from . import models
from .models import Fish, Category, Species
from users.models import Group
from django.contrib.auth import get_user_model


class FishResource(resources.ModelResource):
    category = Field(attribute='category', column_name='category', widget=ForeignKeyWidget(Category, 'name'))
    species = Field(attribute='species', column_name='species', widget=ForeignKeyWidget(Species, 'name'))
    maintainer = Field(attribute='maintainer', column_name='maintainer', widget=ForeignKeyWidget(get_user_model(), 'name'))
    ownership = Field(attribute='ownership', column_name='ownership', widget=ForeignKeyWidget(Group, 'name'))
    
    class Meta:
        model = Fish
        skip_unchanged = True
        clean_model_instances = True
        exclude = ('id', 'created', 'modified')
        export_order = ('species', 'category', 'strain_name', 'common_name', 'line_number', 'background', 
                        'genotype', 'phenotype', 'origin',
                        'availability', 'link', 'quarantine', 'mta', 'public', 'line_description', 'comments',
                        'maintainer', 'ownership')

class FishAdmin(ImportMixin, ExportActionMixin, admin.ModelAdmin):
    resource_class = FishResource
    readonly_fields = ["created", "modified"]

admin.site.register(Fish, FishAdmin)
admin.site.register(models.Species)
admin.site.register(models.Category)
admin.site.register(models.Location)
