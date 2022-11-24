from django.urls import include, path
from rest_framework.routers import DefaultRouter

from order_payment.views import OrderDetailViewSet, OrderViewSet


router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order_detail', OrderDetailViewSet, basename='order_detail')



urlpatterns = [
    path('', include(router.urls)),
]