from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'species'
        verbose_name_plural = 'species'

    def __str__(self):
        return self.name
