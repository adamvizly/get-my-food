from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class DeliveryRequest(models.Model):
    class AttainType(models.IntegerChoices):
        CARD = 1, _("Card")
        CODE = 2, _("Code")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    from_address = models.TextField()
    to_address = models.TextField()
    attain_type = models.IntegerField(choices=AttainType, default=AttainType.CODE)
    code = models.CharField(max_length=25, null=True, blank=True)
    delivery_time = models.DateTimeField()
    accepted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cost = models.FloatField()


class Delivery(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request = models.ForeignKey(DeliveryRequest, on_delete=models.CASCADE)
    delivered_at = models.DateTimeField()
    delivered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
