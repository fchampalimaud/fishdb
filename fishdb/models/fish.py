# from .zebrafish_queryset import FishQuerySet
# from .zebrafish_permission import ZebrafishPermission
from .zebrafish_base import AbstractFish


# class Fish(AbstractFish):

#     objects = FishQuerySet.as_manager()

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         if self.lab is not None:
#             ZebrafishPermission.objects.get_or_create(zebrafish=self, group=self.lab, viewonly=False)
