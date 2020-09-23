from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CartViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls))
]
