from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import DeliveryRequest, Delivery
from .forms import CustomUserCreationForm, RequestForm

UserModel = get_user_model()

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class SignOut(generic.TemplateView):
    template_name = "home.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)

class DeliveryRequestListView(ListView):
    model = DeliveryRequest
    context_object_name = 'requests'  

class DeliveryRequestDetailView(DetailView):        
    model = DeliveryRequest
    context_object_name = 'request'   

class DeliveryRequestCreateView(CreateView):   
    form_class = RequestForm
    model = DeliveryRequest
    success_url = reverse_lazy("request-list")
    
    def form_valid(self, form):
        user = get_object_or_404(UserModel, pk=self.request.user.id)
        form.instance.created_by = user
        response = super(DeliveryRequestCreateView, self).form_valid(form)
        return response

class DeliveryRequestUpdateView(UpdateView):   
    form_class = RequestForm
    model = DeliveryRequest
    success_url = reverse_lazy("request-list")

class DeliveryRequestDeleteView(DeleteView):
    model = DeliveryRequest
    success_url = reverse_lazy("request-list")


class DeliveryListView(ListView):
    model = Delivery
    context_object_name = 'deliveries'  

class DeliveryDetailView(DetailView):         
    model = Delivery
    context_object_name = 'delivery'   

class DeliveryCreateView(CreateView):    
    model = Delivery
    fields = ['request', 'delivered_at', 'delivered_by']
    success_url = reverse_lazy("delivery-list")

class DeliveryUpdateView(UpdateView):     
    model = Delivery  
    fields = ['request', 'delivered_at', 'delivered_by']
    success_url = reverse_lazy("delivery-list") 

class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = reverse_lazy("delivery-list")
