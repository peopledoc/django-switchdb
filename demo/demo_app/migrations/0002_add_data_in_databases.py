# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 09:52
from __future__ import unicode_literals

from django.db import migrations


def add_data_in_database(apps, schema_editor):
    ItemForTest = apps.get_model('demo_app', 'ItemForTest')

    if schema_editor.connection.alias == 'default':
        ItemForTest.objects.using('default').create(name='Item1')
        ItemForTest.objects.using('default').create(name='Item2')

    if schema_editor.connection.alias == 'other_database':
        ItemForTest.objects.using('other_database').create(name='DB2_Item1')
        ItemForTest.objects.using('other_database').create(name='DB2_Item2')
        ItemForTest.objects.using('other_database').create(name='DB2_Item3')


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_data_in_database)]
