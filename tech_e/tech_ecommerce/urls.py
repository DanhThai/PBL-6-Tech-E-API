
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tech_ecommerce.views import CategoryViewSet, ImgProductViewSet, OptionViewSet, ProductChildViewSet, ProductList, ProductVariantViewSet, ProductViewSet, SpeficicationViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product_crud')
router.register(r'category', CategoryViewSet, basename='category_crud')
router.register(r'img-product', ImgProductViewSet, basename='img_crud')
router.register(r'speficication', SpeficicationViewSet, basename='speficication')
router.register(r'product-child', ProductChildViewSet, basename='product_child')
router.register(r'product-variant', ProductVariantViewSet, basename='product_variant')
router.register(r'option', OptionViewSet, basename='option')



urlpatterns = [
    path('', include(router.urls)),
    path('product-list', ProductList.as_view())
]