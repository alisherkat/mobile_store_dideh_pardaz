import json
import random
from unittest import TestCase

from django.db.models import F
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Brand, Mobile
from store.serializers import MobileSerializers


def create_brand(name="Applew", nationality="USAw"):
    return Brand.objects.get_or_create(name=name, nationality=nationality)[0]


def create_mobile(**params):
    brand = create_brand()
    """Create and return a sample recipe."""
    defaults = {
        'model_name': 'Apple iPhone 12+',
        'price': 1000.0,
        'color': "gold",
        'size': 6.1,
        'is_available': False,
        'country': 'China',
        'brand': brand
    }
    defaults.update(params)
    mobile = Mobile.objects.create(**defaults)
    return mobile


class StoreTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_korean_brand(self):
        # brand = create_brand("samsung", "Korea")
        # create_mobile(brand=brand)
        korea_url = reverse("mobile_with_brand_country", args=['Korea'])
        res = self.client.get(korea_url)
        mobiles = Mobile.objects.filter(brand__nationality="Korea")
        serializer = MobileSerializers(mobiles, many=True)
        res_content = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res_content, serializer.data)

    def test_get_brand(self):
        brand = "Apple"
        #
        # create_mobile(model_name="galaxy s312q")
        # create_mobile(model_name="galaxy s412q")
        brand_url = reverse("get_mobile_with_brand_name")
        res = self.client.post(brand_url, {"brand": brand})
        mobiles = Mobile.objects.filter(brand__name=brand)
        serializer = MobileSerializers(mobiles, many=True)

        res_content = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res_content, serializer.data)

    def test_same_brand_manufacture_nationality(self):
        country = "USA"

        # create_mobile(country=country, model_name="galaxy s312qa")
        # create_mobile(country=country, model_name="galaxy s312qq")
        same_url = reverse("get_same_brand_manufacture_country")
        res = self.client.get(same_url)
        mobiles = Mobile.objects.filter(country=F("brand__nationality"))
        serializer = MobileSerializers(mobiles, many=True)

        res_content = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res_content, serializer.data)

    def test_create_mobile(self):
        defaults = {
            'model_name': f'Apple iPhone 12+{random.randint(0,12345)}',
            'price': 1000.0,
            'color': "gold",
            'size': 6.1,
            'is_available': False,
            'country': 'qKoreasss',
            'brand_name': "samqsung",
            'brand_country': "qKoreasss"
        }
        create_url = reverse("add_mobile")
        res = self.client.post(create_url, defaults)
        mobile = Mobile.objects.get(model_name=defaults['model_name'])
        serializer = MobileSerializers(mobile)

        res_content = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res_content, serializer.data)
