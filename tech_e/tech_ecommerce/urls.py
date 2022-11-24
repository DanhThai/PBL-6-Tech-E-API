
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tech_ecommerce.views import CartItemViewSet, CategoryViewSet, ImgProductViewSet, InteractiveViewSet, OptionViewSet, ProductChildViewSet, ProductList, ProductVariantViewSet, ProductViewSet, SpeficicationViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product_crud')
router.register(r'category', CategoryViewSet, basename='category_crud')
router.register(r'img_product', ImgProductViewSet, basename='img_crud')
router.register(r'speficication', SpeficicationViewSet, basename='speficication')
router.register(r'product_child', ProductChildViewSet, basename='product_child')
router.register(r'product_variant', ProductVariantViewSet, basename='produc_tchild')
router.register(r'option', OptionViewSet, basename='option')
router.register(r'cart_item', CartItemViewSet, basename='cart_item')
router.register(r'interactive', InteractiveViewSet, basename='interactive')



urlpatterns = [
    path('', include(router.urls)),
    path('product-list', ProductList.as_view())
]