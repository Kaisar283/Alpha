from django.db import models
from django.utils.translation import gettext_lazy as _
from countries import Country


class City(models.Model):
    city_name = models.CharField(max_length=70, blank=False, null=False)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.city_name