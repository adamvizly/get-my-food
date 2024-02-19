from django.urls import path
from .views import (
    SignUp, SignOut,
    
    DeliveryRequestListView, DeliveryRequestDetailView, 
    DeliveryRequestCreateView, DeliveryRequestUpdateView,
    DeliveryRequestDeleteView, DeliveryRequestAcceptView,
    
    DeliveryListView, DeliveryCompleteView
)


urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path("signout/", SignOut.as_view(), name="signout"),
    
    path('requests/', DeliveryRequestListView.as_view(), name='request-list'),
    path('requests/<int:pk>/', DeliveryRequestDetailView.as_view(), name='request-detail'), 
    path('requests/new/', DeliveryRequestCreateView.as_view(), name='request-create'),
    path('requests/<int:pk>/update/', DeliveryRequestUpdateView.as_view(), name='request-update'),
    path('requests/<int:pk>/delete/', DeliveryRequestDeleteView.as_view(), name='request-delete'),
    path('requests/<int:pk>/accept/', DeliveryRequestAcceptView.as_view(), name='request-accept'),

    path('deliveries/', DeliveryListView.as_view(), name='delivery-list'),
    path('deliveries/<int:pk>/complete/', DeliveryCompleteView.as_view(), name='delivery-complete'),
]