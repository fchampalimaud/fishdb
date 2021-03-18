from django.conf import settings
from django.db import models
from model_utils import Choices

from fishdb.querysets import FishQuerySet


class Fish(models.Model):

    # =========================================================================
    # WARNING!
    # The following section contain the fields supported by Congento.
    # These should not be modified or else synchronization with Congento
    # database may fail.
    # =========================================================================

    AVAILABILITIES = Choices(
        ("live", "Live"),
        ("cryo", "Cryopreserved"),
        ("both", "Live & Cryopreserved"),
        ("none", "Unavailable"),
    )

    # Fields shared with other congento animal models
    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Updated", auto_now=True)
    availability = models.CharField(max_length=4, choices=AVAILABILITIES)
    link = models.URLField(blank=True)

    # Specific fields for this animal model
    strain_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=50, blank=True)
    species = models.ForeignKey(
        to="fishdb.Species",
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_related",
    )
    category = models.ForeignKey(
        to="fishdb.Category",
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_related",
    )
    background = models.CharField(max_length=30)
    genotype = models.CharField(max_length=30)
    phenotype = models.CharField(max_length=30)
    origin = models.CharField(
        verbose_name="Imported from",
        max_length=80,
        blank=True,
        help_text="Leave blank for in-house generated lines",
    )
    quarantine = models.BooleanField(verbose_name="Quarantine", default=False)
    mta = models.BooleanField(verbose_name="MTA", default=True)
    line_description = models.TextField(blank=True)

    # =========================================================================
    # The following section contain specific fields required by the Fish DB.
    # =========================================================================

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

    class Meta:
        verbose_name = "fish"
        verbose_name_plural = "fish"
        permissions = [("can_import", "Can import from XLSX")]

    def __str__(self):
        return self.strain_name

    def get_origin(self):
        return self.origin or "in-house"

    get_origin.short_description = "Origin"
