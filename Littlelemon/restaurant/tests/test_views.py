from django.test import TestCase
from restaurant.views import menuview, bookingview
from restaurant.models import Menu, Booking
from rest_framework.test import APIClient
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.Menu1 = Menu.objects.create(Title="Ice Cream", Price=8.00, Inventory = 80)
        
    def test_getall(self):
        # Initialize the client
        client = APIClient()

        # Send a GET request to the Menu API endpoint
        response = client.get('/api/menu/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the test instances
        serialized_data = menuSerializer([self.Menu1], many=True).data

        # Check if the response data matches the serialized data
        self.assertEqual(response.data, serialized_data)