from django.core.exceptions import ValidationError
from django.db import models

from model_utils import Choices
from model_utils.models import TimeStampedModel


class Zebrafish(TimeStampedModel):

    LINES = Choices(
        ("wt", "WT"),
        ("tg", "Tg"),
        ("mu", "Mutant"),
        ("cko", "CRISPR KO"),
        ("cki", "CRISPR KI"),
        ("other", "Other"),
    )

    line_name = models.CharField(max_length=20)
    line_number = models.CharField(max_length=20)
    line_type = models.CharField(max_length=5, choices=LINES)
    line_type_other = models.CharField(max_length=20, verbose_name="", blank=True)

    background = models.CharField(max_length=20)
    genotype = models.CharField(max_length=20)
    phenotype = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)

    # Fields shared with other congento animal models

    AVAILABILITIES = Choices(
        ("live", "Live"),
        ("cryo", "Cryopreserved"),
        ("both", "Live & Cryopreserved"),
        ("none", "Unavailable"),
    )

    availability = models.CharField(max_length=4, choices=AVAILABILITIES)
    comments = models.TextField(blank=True)
    link = models.URLField(blank=True)
    mta = models.BooleanField(verbose_name="MTA", default=False)

    # location =
    # contact =
    # pi =

    class Meta:
        verbose_name_plural = "zebrafish"

    def __str__(self):
        return self.line_name

    def clean(self):
        if self.line_type == self.LINES.other:
            if not self.line_type_other:
                raise ValidationError({"line_type_other": "This field is required."})
        else:
            self.line_type_other = ""
