from django.conf import settings
from django.db import models

from fishdb.querysets import FishQuerySet
from fishdb.base_fish import AbstractFish


class Fish(AbstractFish):
    public = models.BooleanField(verbose_name="Public through Congento", default=False)

    # TODO test and fix the two ownership fields
    maintainer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True
    )
    ownership = models.ForeignKey(
        to="users.Group", on_delete=models.PROTECT, null=True, blank=True
    )

    line_number = models.PositiveIntegerField(null=True, blank=True)
    # location = models.ForeignKey(to='fishdb.Location', on_delete=models.PROTECT, related_name='fish')
    comments = models.TextField(blank=True)

    objects = FishQuerySet.as_manager()
