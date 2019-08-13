from django.db import models

from users.mixins import PyformsPermissionsMixin
# FIXME import this when users model is not present
# try:
#     from users.mixins import PyformsPermissionsMixin
# except ImportError:
#     PyformsPermissionsMixin = None
#     # PyformsPermissionsMixin = object


class FishQuerySet(PyformsPermissionsMixin, models.QuerySet):
    ...
