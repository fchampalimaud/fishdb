from .zebrafish_queryset import ZebrafishQuerySet
from .zebrafish_permission import ZebrafishPermission
from .zebrafish_base import ZebrafishBase


class Zebrafish(ZebrafishBase):

    objects = ZebrafishQuerySet.as_manager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.lab is not None:
            ZebrafishPermission.objects.get_or_create(zebrafish=self, group=self.lab, viewonly=False)