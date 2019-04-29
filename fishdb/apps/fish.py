from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from fishdb.models import Zebrafish


class FishApp(ModelAdminWidget):

    UID = 'fishdb'
    MODEL = Zebrafish

    TITLE = 'Zebrafish'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON = 'help'
