from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class SignedOut(generic.TemplateView):
    template_name = "home.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)
