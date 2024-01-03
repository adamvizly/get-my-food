from rest_framework import viewsets
from getter.serializers import DeliverySerializer, DeliveryRequestSerializer
from getter.models import Delivery, DeliveryRequest


class DeliveryRequestViewSet(viewsets.ModelViewSet):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

