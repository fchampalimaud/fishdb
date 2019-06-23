from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Fish


class FishForm(ModelFormWidget):

    FIELDSETS = [
        segment(
            ("species", "category"),
            ("strain_name", "common_name", "line_number", "location"),
            ("background", "genotype", "phenotype", "origin"),
            ("availability", "link"),
            no_columns("mta"),
            no_columns("public"),
            "info:You can use the <b>Line description</b> field below to "
            "provide more details. Use the <b>Comments</b> field below for "
            "private notes.",
            ("line_description", "comments"),
        ),
    ]

    READ_ONLY = ['owner']

    CLOSE_ON_REMOVE = True

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mta.checkbox_type = ""
        self.mta.label_visible = False
        self.public.checkbox_type = ""
        self.public.label_visible = False
        self.public.label = "Share with Congento network"

    @property
    def title(self):
        try:
            return self.model_object.strain_name
        except AttributeError:
            pass  # apparently it defaults to App TITLE

    def get_fieldsets(self, default):
        user = PyFormsMiddleware.user()
        if user.is_superuser:
            default += [("maintainer", "ownership"),]
        return default


class FishApp(ModelAdminWidget):

    UID = 'fishdb'
    MODEL = Fish

    TITLE = 'Fish'

    EDITFORM_CLASS = FishForm

    LIST_DISPLAY = [
        "species",
        "category",
        "strain_name",
        "line_number",
        "genotype",
        "background",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "species",
        "category",
        "location",
        "mta",
        "availability",
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

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 3
    ORQUESTRA_MENU_ICON = 'tint blue'

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True

        if user.memberships.filter(
                group__accesses__animaldb=cls.MODEL._meta.app_label
        ).exists():
            return True

        return False
