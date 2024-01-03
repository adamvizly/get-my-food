from django.db import models
from datetime import datetime
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
    cost = models.FloatField()


class Delivery(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request = models.ForeignKey(DeliveryRequest, on_delete=models.CASCADE)
    delivered_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
