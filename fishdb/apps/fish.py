from confapp import conf
from pyforms.controls import ControlCheckBox
from pyforms_web.organizers import no_columns, segment
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Fish

from users.apps._utils import FormPermissionsMixin
from users.apps._utils import limit_choices_to_database
# FIXME import this when users model is not present


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

        super().__init__(*args, **kwargs)

    def get_toolbar_buttons(self, has_add_permission=False):
        toolbar = super().get_toolbar_buttons(has_add_permission)
        return tuple([toolbar] + ["_inhouse_filter"])

    def get_queryset(self, request, qs):
        if self._inhouse_filter.value:
            qs = qs.filter(origin__exact="")

        return qs

    def get_related_field_queryset(self, request, list_queryset, field, queryset):
        animaldb = self.model._meta.app_label
        queryset = limit_choices_to_database(animaldb, field, queryset)
        return queryset
