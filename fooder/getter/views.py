from datetime import datetime
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import DeliveryRequest, Delivery
from .forms import CustomUserCreationForm, RequestForm


UserModel = get_user_model()


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class SignOut(generic.TemplateView):
    template_name = "home.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryRequestListView(ListView):
    model = DeliveryRequest
    context_object_name = 'requests'  
    
    def get_queryset(self):
        return DeliveryRequest.objects.filter(delivery__delivered_by=None)
    
    def get_context_data(self, **kwargs):
        context = super(DeliveryRequestListView, self).get_context_data(**kwargs)
        context['current_user_id'] = self.request.user.id
        return context


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryRequestDetailView(DetailView):        
    model = DeliveryRequest
    context_object_name = 'request'


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryRequestCreateView(CreateView):   
    form_class = RequestForm
    model = DeliveryRequest
    success_url = reverse_lazy("request-list")
    
    def form_valid(self, form):
        user = get_object_or_404(UserModel, pk=self.request.user.id)
        form.instance.created_by = user
        response = super(DeliveryRequestCreateView, self).form_valid(form)
        return response


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryRequestUpdateView(UpdateView):   
    form_class = RequestForm
    model = DeliveryRequest
    success_url = reverse_lazy("request-list")


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryRequestDeleteView(DeleteView):
    model = DeliveryRequest
    success_url = reverse_lazy("request-list")


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryRequestAcceptView(View):
    def get(self, request, *args, **kwargs):
        request = get_object_or_404(DeliveryRequest, pk=self.kwargs['pk'])
        user = get_object_or_404(UserModel, pk=self.request.user.id)
        delivery = Delivery()
        delivery.request = request
        delivery.delivered_by = user
        delivery.save()
        return HttpResponseRedirect(reverse_lazy("delivery-list"))


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryListView(ListView):
    model = Delivery
    context_object_name = 'deliveries'
    
    def get_queryset(self):
        user = get_object_or_404(UserModel, pk=self.request.user.id)
        return Delivery.objects.filter(delivered_by=user, completed=False)


@method_decorator(login_required(login_url=reverse_lazy("login")), name='dispatch')
class DeliveryCompleteView(View):
    template_name = "getter/delivery_complete.html"
    
    def get(self, request, *args, **kwargs):
        delivery = get_object_or_404(Delivery, pk=self.kwargs['pk'])
        delivery.completed = True
        delivery.delivered_at = datetime.now()
        delivery.save()
        return HttpResponseRedirect(reverse_lazy("delivery-list"))
