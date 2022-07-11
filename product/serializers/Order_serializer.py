from rest_framework import serializers
from product.models import Orders


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Orders
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ('id', 'product', 'sale_price','status_now')


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = "__all__"