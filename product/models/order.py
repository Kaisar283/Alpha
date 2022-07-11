from django.db import models
from accounts.models import CustomUserAccount
from product.models.product import Products
from django.utils import timezone
from utils.consts import OrderStatus
from django.utils.translation import gettext_lazy as _


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status_now = models.CharField(default=OrderStatus.AWAITING_DELIVERY.value, max_length=40)
    owner = models.ForeignKey(CustomUserAccount, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"{self.id} | {self.product} - {self.owner}"