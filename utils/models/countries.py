from django.db import models
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    country_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.country_name


