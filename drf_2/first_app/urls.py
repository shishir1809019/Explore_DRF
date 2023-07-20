from django.urls import include,path
from rest_framework import routers
from .views import ProductViewSet, ProductReviewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', ProductReviewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    # path('api_auth/', include('rest_framework.urls')),
]
