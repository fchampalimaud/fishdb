from django.db import models


class Location(models.Model):
    """Deprecated on 2019 jul 10
    Replaced with a BooleanField to simply track quarantined lines.
    May be reintroduced in the future to manage rooms, cages, systems, etc.
    """
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['name']

    def __str__(self):
        return self.name
