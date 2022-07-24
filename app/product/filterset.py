from django.db.models import Q
from django_filters import rest_framework as filters
from product.models import Orders, Products


class OrderFilterSet(filters.FilterSet):

    class Meta:
        model = Orders
        fields = 'id', 'product', "ordered_date", "status_now"


class ProductFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    search = filters.CharFilter(method='search_by_value', label='search')

    class Meta:
        model = Products
        fields = 'id', 'product_name', "sale_price", "category_id"

    def search_by_value(self, queryset, name, value):
        filter_params = Q()
        W_List = self.request.query_params.get('search').split()
        for word in W_List:
            filter_params |= Q(product_name__contains=word)
        output = queryset.filter(filter_params)
        return output
