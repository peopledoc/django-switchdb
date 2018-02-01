# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import Client
from rest_framework.test import APITestCase

from demo_app.models import ItemForTest


class SwitchDatabaseMiddlewareInAPITestCase(APITestCase):

    def test_number_item_in_each_database(self):
        self.assertEqual(2, ItemForTest.objects.using('default').all().count())
        self.assertEqual(3, ItemForTest.objects.using('other_database').all().count())

    def test_switch_db_first_domain(self):
        c = Client(SERVER_NAME="test1.example.com:8000", HTTP_HOST="test1.example.com:8000")
        response = c.get(reverse('api_items'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, response.data['number_items_for_test'])

    def test_switch_db_second_domain(self):
        c = Client(SERVER_NAME="test2.example.com:8000", HTTP_HOST="test2.example.com:8000")
        response = c.get(reverse('api_items'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(3, response.data['number_items_for_test'])
