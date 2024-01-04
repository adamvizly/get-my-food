from django.urls import path, include
from rest_framework.routers import DefaultRouter

from getter import views
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'delivery', views.DeliveryViewSet, basename='delivery')
router.register(r'request', views.DeliveryRequestViewSet, basename='request')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]