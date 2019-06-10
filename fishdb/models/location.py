from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['name']

    def __str__(self):
        return self.name
