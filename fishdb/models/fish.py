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

    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Updated", auto_now=True)

    species = models.ForeignKey(to='fishdb.Species', on_delete=models.PROTECT, related_name='fish')
    background = models.CharField(max_length=20)
    genotype = models.CharField(max_length=20)
    phenotype = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)

    # Fields shared with other congento animal models
    availability = models.CharField(max_length=4, choices=AVAILABILITIES)
    link = models.URLField(blank=True)
    mta = models.BooleanField(verbose_name="MTA", default=False)

    line_name = models.CharField(max_length=255)
    category = models.ForeignKey(to='fishdb.Category', on_delete=models.PROTECT, related_name='fish')

    class Meta:
        verbose_name = "fish"
        verbose_name_plural = "fish"
        abstract = True

    def __str__(self):
        return self.line_name


class Fish(AbstractFish):
    public = models.BooleanField("Public", default=False)
    owner = models.ForeignKey(to='auth.Group', on_delete=models.PROTECT, null=True, blank=True)

    line_number = models.CharField(max_length=20)  # FIXME FK requested (test)
    comments = models.TextField(blank=True)
