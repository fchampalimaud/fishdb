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
    mta = models.BooleanField(verbose_name="MTA", default=False)

    # Specific fields for this animal model
    line_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=50, blank=True)
    species = models.ForeignKey(to='fishdb.Species', on_delete=models.PROTECT, related_name='fish')
    category = models.ForeignKey(to='fishdb.Category', on_delete=models.PROTECT, related_name='fish')
    background = models.CharField(max_length=30)
    genotype = models.CharField(max_length=30)
    phenotype = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)
    line_description = models.TextField(blank=True)

    class Meta:
        verbose_name = "fish"
        verbose_name_plural = "fish"
        abstract = True

    def __str__(self):
        return self.line_name


class Fish(AbstractFish):
    public = models.BooleanField("Public", default=False)

    # TODO test and fix the two ownership fields
    maintainer = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    ownership = models.ForeignKey(to="auth.Group", on_delete=models.PROTECT, null=True, blank=True)

    line_number = models.PositiveIntegerField()
    location = models.ForeignKey(to='fishdb.Location', on_delete=models.PROTECT, related_name='fish')
    comments = models.TextField(blank=True)
