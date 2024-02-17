from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signup"),
    path("signout/", views.SignedOut.as_view(), name="signout"),
]