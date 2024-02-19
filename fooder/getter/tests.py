from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from .models import Delivery, DeliveryRequest
from datetime import datetime


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(phone="9147146122", password="foo")
        self.assertEqual(user.phone, "9147146122")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(phone="")
        with self.assertRaises(ValueError):
            User.objects.create_user(phone="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(phone="9147146122", password="foo")
        self.assertEqual(admin_user.phone, "9147146122")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone="9147146122", password="foo", is_superuser=False)
        

class DeliveryRequestViewsTests(TestCase):
    
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(phone="9147146122", password="foo")
        self.client.force_login(self.user)
        self.request_data = {
            'from_address': 'mabda', 
            'to_address': 'maghsad',
            'delivery_time': datetime(2023, 2, 25, 9, 0),
            'created_by': self.user,
            'cost': 9.99,
        }
        self.delivery_request = DeliveryRequest.objects.create(**self.request_data)

    def test_request_list_view(self):
        response = self.client.get(reverse_lazy('request-list'))
        self.assertEqual(response.status_code, 200)

    def test_request_detail_view(self):
        url = reverse_lazy('request-detail', args=[self.delivery_request.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_request_create_view(self):
        response = self.client.post(reverse_lazy('request-create'), self.request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(DeliveryRequest.objects.count(), 1)  
        self.assertEqual(DeliveryRequest.objects.last().cost, 9.99)

    def test_request_update_view(self):
        url = reverse_lazy('request-update', args=[self.delivery_request.id])
        data = self.request_data.copy()
        data['cost'] = 9.99
        response = self.client.post(url, data)
        self.delivery_request.refresh_from_db()
        self.assertEqual(self.delivery_request.cost, 9.99)
      
    def test_request_delete_view(self):
        url = reverse_lazy('request-delete', args=[self.delivery_request.id]) 
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(DeliveryRequest.objects.filter(id=self.delivery_request.id).exists())    
