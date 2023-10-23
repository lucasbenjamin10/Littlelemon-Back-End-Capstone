from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Ice Cream", Price=8.00, Inventory=100)
        self.assertEqual(item, "Ice Cream : 80")