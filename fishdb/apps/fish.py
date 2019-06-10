from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Fish


class FishForm(ModelFormWidget):

    FIELDSETS = [
        'public',
        ("line_name", "line_number", "line_type", "line_type_other"),
        ("background", "genotype", "phenotype", "origin"),
        ("availability", "mta"),
        "link",
        "comments",
    ]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mta.checkbox_type = ""

        self.line_type_other.label = "&nbsp"
        self.line_type.changed_event = self.__on_line_type

        self.__on_line_type()

    @property
    def title(self):
        try:
            return self.model_object.line_name
        except AttributeError:
            pass  # apparently it defaults to App TITLE

    def __on_line_type(self):
        if self.line_type.value == "other":
            self.line_type_other.show()
        else:
            self.line_type_other.hide()


class FishApp(ModelAdminWidget):

    UID = 'fishdb'
    MODEL = Fish

    TITLE = 'Fish'

    EDITFORM_CLASS = FishForm

    LIST_DISPLAY = [
        "line_name",
        "line_number",
        "line_type",
        "background",
        "genotype",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "line_type",
        "mta",
        "availability",
    ]

    SEARCH_FIELDS = [
        "line_name__icontains",
        "line_number__icontains",
        "line_type__icontains",
        "background__icontains",
        "genotype__icontains",
        "origin__icontains",
    ]

    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 3
    ORQUESTRA_MENU_ICON = 'tint blue'
