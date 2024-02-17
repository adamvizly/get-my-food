from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signup"),
    path("signout/", views.SignedOut.as_view(), name="signout"),
    path("delivery/", views.SignedOut.as_view(), name="delivery"),
    path("delivery/request/", views.SignedOut.as_view(), name="delivery-request"),
    path("delivery/request/delete/", views.SignedOut.as_view(), name="delivery-request-delete"),
    path("delivery/accept/", views.SignedOut.as_view(), name="delivery-accept"),
]