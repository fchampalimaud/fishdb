from django.db import models


class Line(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'line'
        verbose_name_plural = 'lines'
        ordering = ['name']

    def __str__(self):
        return self.name
