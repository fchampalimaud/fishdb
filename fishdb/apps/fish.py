from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Fish


class FishForm(ModelFormWidget):

    FIELDSETS = [
        'public',
        "species",
        ("line_name", "line_number", "category", "common_name"),
        ("background", "genotype", "phenotype", "origin"),
        "location",
        ("availability", "mta"),
        "link",
        ("comments", "line_description"),
        ("maintainer", "ownership"),
    ]

    READ_ONLY = ['owner']

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mta.checkbox_type = ""

    @property
    def title(self):
        try:
            return self.model_object.line_name
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class FishApp(ModelAdminWidget):

    UID = 'fishdb'
    MODEL = Fish

    TITLE = 'Fish'

    EDITFORM_CLASS = FishForm

    LIST_DISPLAY = [
        "line_name",
        "line_number",
        "category",
        "species",
        "background",
        "genotype",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "category",
        "species",
        "mta",
        "availability",
    ]

    SEARCH_FIELDS = [
        "line_name__icontains",
        "line_number__icontains",
        "category__icontains",
        "background__icontains",
        "genotype__icontains",
        "origin__icontains",
    ]

    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 3
    ORQUESTRA_MENU_ICON = 'tint blue'
