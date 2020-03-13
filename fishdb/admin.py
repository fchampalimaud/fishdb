from django.contrib import admin
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import FieldDoesNotExist
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
    maintainer = Field(attribute='maintainer', column_name='maintainer', widget=ForeignKeyWidget(get_user_model(), 'email'))
    ownership = Field(attribute='ownership', column_name='ownership', widget=ForeignKeyWidget(Group, 'name'))
    
    class Meta:
        model = Fish
        skip_unchanged = True
        clean_model_instances = True
    
    def before_import_row(self, row, **kwargs):
        for field, value in row.items():
            if field in self._date_fields:
                # check if the value is a float and convert to datetime here
                tz = timezone.get_current_timezone()
                if isinstance(value, float):
                    import xlrd
                    row[field] = tz.localize(datetime(*xlrd.xldate_as_tuple(value, 0)))
                elif isinstance(value, datetime):
                    # we need to add the timezone to the datetime
                    row[field] = tz.localize(value)
            if value is None:
                # check default value for this field within the model and set it in the row value before proceeding
                try:
                    f = self._meta.model._meta.get_field(field)
                except FieldDoesNotExist:
                    continue
                if f.blank is True and f.null is False:
                    row[field] = ''

        return super().before_import_row(row, **kwargs)

class FishAdmin(ImportMixin, ExportActionMixin, admin.ModelAdmin):
    resource_class = FishResource
    readonly_fields = ["created", "modified"]

admin.site.register(Fish, FishAdmin)
admin.site.register(models.Species)
admin.site.register(models.Category)
admin.site.register(models.Location)
