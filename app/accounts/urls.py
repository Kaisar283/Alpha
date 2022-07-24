from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountAuthViewSet

router = DefaultRouter()
router.register(r'auth', AccountAuthViewSet, basename='auth')

urlpatterns = [] + router.urls