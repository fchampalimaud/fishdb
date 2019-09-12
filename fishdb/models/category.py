from django.db import models


class AbstractCategory(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name"]
        abstract = True

    def __str__(self):
        return self.name


class Category(AbstractCategory):
    ...
