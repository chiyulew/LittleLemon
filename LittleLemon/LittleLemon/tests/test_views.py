from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.menu1 = Menu.objects.create(name="Menu1", description="description1")
        self.menu2 = Menu.objects.create(name="Menu2", description="description2")
        
    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menus = Menu.objects.all()
        
        serializer = MenuSerializer(menus, many=True)
        
        self.asserEqual(response.data, serializer.date)