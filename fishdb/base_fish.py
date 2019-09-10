from django.conf import settings
from django.db import models
from model_utils import Choices


class AbstractFish(models.Model):
    """
    Must be compatible with Congento model scheme!
    """

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
        to="fishdb.Species", on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related"
    )
    category = models.ForeignKey(
        to="fishdb.Category", on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related"
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

    class Meta:
        verbose_name = "fish"
        verbose_name_plural = "fish"
        abstract = True

    def __str__(self):
        return self.strain_name

    def get_origin(self):
        # FIXME get correct isntitution name after from configuration (settings or DB)
        return self.origin or getattr(settings, "INSTITUTION_NAME", "in-house")

    get_origin.short_description = "Origin"
