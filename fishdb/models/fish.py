from django.core.exceptions import ValidationError
from django.db import models

from model_utils import Choices


class AbstractFish(models.Model):
    """
    Must be compatible with Congento model scheme!
    """

    LINES = Choices(
        ("wt", "WT"),
        ("tg", "Tg"),
        ("mu", "Mutant"),
        ("cko", "CRISPR KO"),
        ("cki", "CRISPR KI"),
        ("other", "Other"),
    )

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
    comments = models.TextField(blank=True)
    link = models.URLField(blank=True)
    mta = models.BooleanField(verbose_name="MTA", default=False)

    line_name = models.CharField(max_length=20)
    line_number = models.CharField(max_length=20)
    line_type = models.CharField(max_length=5, choices=LINES)
    line_type_other = models.CharField(max_length=20, verbose_name="", blank=True)

    class Meta:
        verbose_name = "fish"
        verbose_name_plural = "fish"
        abstract = True

    def __str__(self):
        return self.line_name

    def clean(self):
        if self.line_type == self.LINES.other:
            if not self.line_type_other:
                raise ValidationError({"line_type_other": "This field is required."})
        else:
            self.line_type_other = ""


class Fish(AbstractFish):
    public = models.BooleanField("Public", default=False)
