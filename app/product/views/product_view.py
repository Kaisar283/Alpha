from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from product.serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from product.models import Products
from rest_framework.response import Response
from django_filters import rest_framework as filters
from product.filterset import ProductFilterSet


class ProductViewSet(GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]
    queryset = Products.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ProductFilterSet

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        return serializer_class

    @action(methods=['get'], detail=False, url_path='product_list')
    def get_owner_order(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.queryset.all())
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)