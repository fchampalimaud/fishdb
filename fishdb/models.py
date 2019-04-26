from django.db import models

from model_utils import Choices


class Zebrafish(models.Model):

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

    background = models.CharField(max_length=20)
    genotype = models.CharField(max_length=20)
    phenotype = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)

    # Fields shared with other congento animal models

    AVAILABILITIES = Choices(
        ("live", "Live"), ("cryo", "Cryopreserved"), ("both", "Live & Cryopreserved")
    )

    availability = models.CharField(max_length=4, choices=AVAILABILITIES)
    comments = models.TextField()
    link = models.URLField()
    mta = models.BooleanField(verbose_name="MTA", default=False)

    # location =
    # contact =
    # pi =
