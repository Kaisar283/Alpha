from django.db import models
from product.models.category import Categories
from django.utils.translation import gettext_lazy as _


class Products(models.Model):
    product_name = models.CharField(max_length=60)
    quantity = models.SmallIntegerField(blank=True)
    sale_price = models.IntegerField(blank=False)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f"{self.id} | {self.product_name}"
