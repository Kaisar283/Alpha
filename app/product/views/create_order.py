from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from product.serializers import OrderSerializer, OrderListSerializer, OrderUpdateSerializer, Create_Order_PDF
from product.models import Orders
from django_filters import rest_framework as filters
from product.filterset import OrderFilterSet


class CreateOrderViewSet(GenericViewSet):
    serializer_class = Create_Order_PDF
    permission_classes = [IsAuthenticated, ]
    queryset = Orders.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = OrderFilterSet

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == "create_order":
            serializer_class = OrderSerializer
        elif self.action == "my_orders":
            serializer_class = OrderListSerializer
        elif self.action == "update_status":
            serializer_class = OrderUpdateSerializer
        elif self.action == "my_order_list_pdf":
            serializer_class = Create_Order_PDF
        return serializer_class

    def get_permissions(self):
        permissions_classes = self.permission_classes
        if self.action == "create_order" or self.action == "my_orders":
            permissions_classes = [IsAuthenticated, ]
        return [permission() for permission in permissions_classes]

    @action(methods=['post'], detail=False, url_path='create_order')
    def create_order(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False, url_path='my_orders')
    def get_owner_order(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.filter(owner=request.user), many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='my_order_list_pdf')
    def get_pdf_order_list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={"id": request.user.id, "email": request.user.email})
        serializer.is_valid()
        serializer.create_PDF()
        return Response(data={"detail": "Your PDF document is creating, as soon as it is ready, we will send you"})



