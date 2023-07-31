import random
from unittest import TestCase

from core.models import Brand, Mobile


def create_brand(name="Appleq", nationality="USAq"):
    return Brand.objects.get_or_create(name=name, nationality=nationality)[0]


class ModelTest(TestCase):
    def test_create_brand(self):
        name = "Appler"
        nationality = "USAr"
        brand = create_brand(name, nationality)
        self.assertEqual(brand.name, name)
        self.assertEqual(brand.nationality, nationality)

    def test_create_mobile(self):
        brand = create_brand()
        model_name = f"galaxy s20 black{random.randint(0,15000)}"
        price = float(700)
        color = "black"
        size = 6.50
        is_available = True
        country = "Korea"
        mobile = Mobile.objects.create(brand=brand, model_name=model_name, price=price, color=color,
                                       size=size, is_available=is_available, country=country)
        self.assertEqual(mobile.brand.name, brand.name)
        self.assertEqual(mobile.brand.nationality, brand.nationality)
        self.assertEqual(mobile.model_name, model_name)
        self.assertEqual(mobile.price, price)
        self.assertEqual(mobile.color, color)
        self.assertEqual(mobile.size, size)
        self.assertEqual(mobile.is_available, is_available)
        self.assertEqual(mobile.country, country)
