from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from product.views import CreateOrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'order', CreateOrderViewSet, basename='order')
router.register(r'product_info', ProductViewSet, basename='product_info')


urlpatterns = [
    # path('product_list', ProductViewSet.as_view())
] + router.urls