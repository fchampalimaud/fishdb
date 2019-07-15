from django.db import models
from django.db.models import Q

from fishdb.mixins import PyformsPermissionsMixin

class FishQuerySet(PyformsPermissionsMixin, models.QuerySet):
    ...
