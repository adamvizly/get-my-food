from django.urls import path
from . import views
from .views import (
    SignUp, SignOut,
    
    DeliveryRequestListView, DeliveryRequestDetailView, 
    DeliveryRequestCreateView, DeliveryRequestUpdateView,
    DeliveryRequestDeleteView,
    
    DeliveryListView, DeliveryDetailView,
    DeliveryCreateView, DeliveryUpdateView, 
    DeliveryDeleteView
)


urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path("signout/", SignOut.as_view(), name="signout"),
    
    path('requests/', DeliveryRequestListView.as_view(), name='request-list'),
    path('requests/<int:pk>/', DeliveryRequestDetailView.as_view(), name='request-detail'), 
    path('requests/new/', DeliveryRequestCreateView.as_view(), name='request-create'),
    path('requests/<int:pk>/update/', DeliveryRequestUpdateView.as_view(), name='request-update'),
    path('requests/<int:pk>/delete/', DeliveryRequestDeleteView.as_view(), name='request-delete'),

    path('deliveries/', DeliveryListView.as_view(), name='delivery-list'),
    path('deliveries/<int:pk>/', DeliveryDetailView.as_view(), name='delivery-detail'),
    path('deliveries/new/', DeliveryCreateView.as_view(), name='delivery-create'), 
    path('deliveries/<int:pk>/update/', DeliveryUpdateView.as_view(), name='delivery-update'),
    path('deliveries/<int:pk>/delete/', DeliveryDeleteView.as_view(), name='delivery-delete'),
]