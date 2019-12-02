from confapp import conf
from django.views import View
from pyforms.controls import ControlCheckBox, ControlButton, ControlFileUpload
from pyforms_web.basewidget import BaseWidget
from pyforms_web.organizers import no_columns, segment
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Fish
from fishdb.admin import FishResource

from users.apps._utils import FormPermissionsMixin
from users.apps._utils import limit_choices_to_database
from django.shortcuts import redirect
from tablib.core import Dataset, UnsupportedFormat
import os
# FIXME import this when users model is not present


class FishImportWidget(BaseWidget):
    TITLE = 'Import Fish'   
    
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW
    CREATE_BTN_LABEL = '<i class="upload icon"></i>Import'
    HAS_CANCEL_BTN_ON_ADD = False

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._csv_file = ControlFileUpload(label='Import CSV')
        self._import_btn = ControlButton(
            '<i class="upload icon"></i>Import',
            default=self.__import_evt,
            label_visible=False,
            css='basic blue',
            helptext='Import Fish from CSV file',
        )

        self.formset = [
            '_csv_file',
            '_import_btn'
        ]

    def __import_evt(self):

        fish_resource = FishResource()

        if self._csv_file.filepath is not None:
            dataset = Dataset()

            try:
                with open(self._csv_file.filepath, 'r') as f:
                    imported_file = dataset.load(f.read())
            except UnsupportedFormat as uf:
                raise Exception("Unsupported format. Please select a CSV file with the Fish template columns")

            # Test the import first
            result = fish_resource.import_data(dataset, dry_run=True, use_transactions=True, collect_failed_rows=True)
            if result.has_validation_errors():
                val_errors = ''
                for err in result.invalid_rows:
                    val_errors += f'row {err.number}:<br><ul>'
                    for key in err.field_specific_errors:
                        val_errors += f'<li>{key} &rarr; {err.field_specific_errors[key][0]}</li>'
                    val_errors += '</ul>'
                raise Exception(f"Validation error(s) on row(s): {', '.join([str(err.number) for err in result.invalid_rows])} <br>{val_errors}")
            elif result.has_errors():
                raise Exception(f"Error detected that prevents importing on row(s): {', '.join([str(num) for num, _ in result.row_errors()])}")
            else:
                fish_resource.import_data(dataset, dry_run=False, use_transactions=True)
            
            self.success("Fish file imported successfully!")


class FishForm(FormPermissionsMixin, ModelFormWidget):

    CLOSE_ON_REMOVE = True

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.quarantine.checkbox_type = ""
        self.quarantine.label_visible = False
        self.mta.checkbox_type = ""
        self.mta.label_visible = False
        self.public.checkbox_type = ""
        self.public.label_visible = False

    @property
    def title(self):
        try:
            return self.model_object.strain_name
        except AttributeError:
            pass  # apparently it defaults to App TITLE

    def get_fieldsets(self, default):

        default = [
            segment(
                ("species", "category"),
                ("strain_name", "common_name", "line_number", " "),
                ("background", "genotype", "phenotype", "origin"),
                ("availability", "link"),
                no_columns("quarantine"),
                no_columns("mta"),
                no_columns("public"),
                "info:You can use the <b>Line description</b> field below to "
                "provide more details. Use the <b>Comments</b> field below for "
                "private notes.",
                ("line_description", "comments"),
            )
        ]
        if self.object_pk:  # editing existing object
            default += [("maintainer", "ownership", "created", "modified")]

        return default

    def get_related_field_queryset(self, field, queryset):
        animaldb = self.model._meta.app_label
        queryset = limit_choices_to_database(animaldb, field, queryset)
        return queryset


class FishApp(ModelAdminWidget):

    UID = "fishdb"
    MODEL = Fish

    TITLE = "Fish"

    EDITFORM_CLASS = FishForm

    LIST_DISPLAY = [
        "species",
        "category",
        "strain_name",
        "line_number",
        "genotype",
        "background",
        "get_origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "species",
        "category",
        "quarantine",
        # "location",
        "mta",
        "availability",
        "public",
        "maintainer",
        "ownership",
    ]

    SEARCH_FIELDS = [
        "strain_name__icontains",
        "common_name__icontains",
        "background__icontains",
        "genotype__icontains",
        "phenotype__icontains",
        "origin__icontains",
        "line_description__icontains",
        "line_number__icontains",
        "comments__icontains",
    ]

    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    STATIC_FILES = ['fishdb/icon.css']  # required for the menu icon CSS

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "left"
    ORQUESTRA_MENU_ORDER = 3
    ORQUESTRA_MENU_ICON = "large congento-fish"

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True

        if user.memberships.filter(
            group__accesses__animaldb=cls.MODEL._meta.app_label
        ).exists():
            return True

        return False

    def __init__(self, *args, **kwargs):

        self._inhouse_filter = ControlCheckBox(
            "List only in-house generated lines",
            default=False,
            label_visible=False,
            changed_event=self.populate_list,
        )

        self._import_btn = ControlButton(
            '<i class="upload icon"></i>Import',
            default=self.__import_evt,
            label_visible=False,
            css='basic blue',
            helptext='Import Fish from CSV file',
        )

        super().__init__(*args, **kwargs)

    def get_toolbar_buttons(self, has_add_permission=False):
        toolbar = super().get_toolbar_buttons(has_add_permission)
        return tuple([no_columns(toolbar, "_import_btn")] + [" ", "_inhouse_filter"])

    def get_queryset(self, request, qs):
        if self._inhouse_filter.value:
            qs = qs.filter(origin__exact="")

        return qs

    def get_related_field_queryset(self, request, list_queryset, field, queryset):
        animaldb = self.model._meta.app_label
        queryset = limit_choices_to_database(animaldb, field, queryset)
        return queryset

    def __import_evt(self):
        FishImportWidget(parent_win=self)
