from django.db import models
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    category_name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    discription = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f"{self.id} | {self.category_name}"