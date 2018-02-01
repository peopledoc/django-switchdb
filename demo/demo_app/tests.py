# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from .models import ItemForTest

from django_switchdb.db_selector import get_database_depending_queryset_result


class SwitchDatabaseMiddlewareTestCase(TestCase):

    def test_number_item_in_each_database(self):
        self.assertEqual(2, ItemForTest.objects.using('default').all().count())
        self.assertEqual(3, ItemForTest.objects.using('other_database').all().count())

    def test_switch_db_first_domain(self):

        c = Client(SERVER_NAME="test1.example.com:8000", HTTP_HOST="test1.example.com:8000")
        response = c.get(reverse('items'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, response.context_data['number_items'])

    def test_switch_db_second_domain(self):

        c = Client(SERVER_NAME="test2.example.com:8000", HTTP_HOST="test2.example.com:8000")
        response = c.get(reverse('items'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(3, response.context_data['number_items'])


class SwitchDependOnQuerysetTestCase(TestCase):

    def test_switch_db_first_database(self):
        query = ItemForTest.objects.filter(name="Item1")
        self.assertEqual('default', get_database_depending_queryset_result(query))

    def test_switch_db_second_database(self):
        query = ItemForTest.objects.filter(name="DB2_Item1")
        self.assertEqual('other_database', get_database_depending_queryset_result(query))
