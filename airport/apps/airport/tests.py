from django.test import TestCase
from django.test import Client


from .models import *


class TestAirport(TestCase):

    def test_instantiate_country(self):
        country = Country('NL', 'The Netherlands', 'europe/amsterdam')
        self.assertIsInstance(country, Country)

    def test_save_country(self):
        country = Country('NL', 'The Netherlands', 'europe/amsterdam')
        country.save()
        country = Country('B', 'Germany', 'europe/amsterdam')
        country.save()
        qs = Country.objects.all()
        actual = len(qs)
        expected = 2
        self.assertEqual(actual, expected)

    def test_get(self):
        c = Client()
        response = c.get("/airport/countries")
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)