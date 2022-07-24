from rest_framework import serializers
from product.models import Orders
from product.tasks import order_pdf_creater
from accounts.models import CustomUserAccount


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


class Create_Order_PDF(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()

    def create_PDF(self):
        id = self.validated_data.get('id')
        email = self.validated_data.get('email')
        order_pdf_creater.delay(id, email)

