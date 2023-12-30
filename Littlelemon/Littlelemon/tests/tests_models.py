from django.test import TestCase
from restaurant.models import *
from restaurant.serializers import *

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item=menuSerializer(data=item)
        self.assertEqual(item, "IceCream : 80")