from django.urls import path, include
from rest_framework.routers import DefaultRouter

from getter import views

router = DefaultRouter()
router.register(r'delivery', views.DeliveryViewSet, basename='delivery')
router.register(r'request', views.DeliveryRequestViewSet, basename='request')


urlpatterns = [
    path('', include(router.urls)),
]