from rest_framework import serializers
from getter.models import Delivery, DeliveryRequest


class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = ['from_address', 'to_address', 'attain_type', 'code', 'delivery_time', 'cost', 'created_at']


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['request', 'delivered_at', 'completed']
