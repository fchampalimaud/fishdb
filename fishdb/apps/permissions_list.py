from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget
from fishdb.models import ZebrafishPermission



class PermissionsListApp(ModelAdminWidget):

    MODEL = ZebrafishPermission
    TITLE = 'Permissions'

    LIST_DISPLAY = ['group', 'viewonly']
    FIELDSETS    = [ ('group', 'viewonly') ]