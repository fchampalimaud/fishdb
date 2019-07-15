from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from fishdb.models import Category


class FishCategoryForm(ModelFormWidget):

    FIELDSETS = ["name"]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW


class FishCategoryApp(ModelAdminWidget):

    UID = "fish-categories"
    MODEL = Category

    TITLE = "Categories"

    EDITFORM_CLASS = FishCategoryForm

    USE_DETAILS_TO_ADD = False  # required to have form in NEW_TAB
    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "left>FishApp"
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = "cog"

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser or user.is_admin(cls.MODEL._meta.app_label):
            return True
        return False
