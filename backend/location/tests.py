from django.test import TestCase, Client
from .models import Location

import json


class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(name='loc_name_1', latitude = -11.1111111, longitude = 22.2222222)
        Location.objects.create(name='loc_name_2', latitude = 33.1141411, longitude = -123.2222222)
        Location.objects.create(name='loc_name_3', latitude = 67.1122111, longitude = 161.2222222)
    
    def test_get_location_id(self):
        client = Client()
        response = client.get('/api/location/1/')

        self.assertEqual(response.status_code, 201)
        self.assertIn('-11.1111111', response.content.decode())


# Create your tests here.
