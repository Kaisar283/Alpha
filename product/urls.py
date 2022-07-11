from rest_framework.routers import DefaultRouter
from product.views import CreateOrderViewSet

router = DefaultRouter()
router.register(r'order', CreateOrderViewSet, basename='order')

urlpatterns = [] + router.urls