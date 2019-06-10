from django.db import models


class ZebrafishPermission(models.Model):


    viewonly  = models.BooleanField('Read only access')
    fish = models.ForeignKey('Fish',  on_delete=models.CASCADE)
    group     = models.ForeignKey('auth.Group', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(
            str(self.zebrafish),
            str(self.group),
            str(self.viewonly)
        )

    class Meta:
        verbose_name = "Zebrafish permission"
        verbose_name_plural = "Zebrafishs permissions"

        unique_together = (
            ('fish', 'group'),
        )
