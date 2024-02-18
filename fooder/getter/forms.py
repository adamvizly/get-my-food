from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, widgets
from .models import CustomUser, DeliveryRequest


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("phone", "first_name", "last_name",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("phone", "first_name", "last_name",)


class RequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['from_address', 'to_address', 'attain_type', 'code', 'delivery_time', 'cost']
        widgets = {
            'delivery_time': widgets.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
        }
