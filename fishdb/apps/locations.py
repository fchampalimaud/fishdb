from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Location


class FishLocationForm(ModelFormWidget):

    FIELDSETS = ["name"]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW


class FishLocationApp(ModelAdminWidget):

    UID = 'fish-locations'
    MODEL = Location

    TITLE = 'Locations'

    EDITFORM_CLASS = FishLocationForm

    USE_DETAILS_TO_ADD = False  # required to have form in NEW_TAB
    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left>FishApp'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'cog'

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True
        return False
