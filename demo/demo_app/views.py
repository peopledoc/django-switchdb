# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from django.views.generic import TemplateView

from django_switchdb.db_selector import get_database_depending_queryset_result

from .models import ItemForTest


class ItemForTestView(TemplateView):
    template_name = "demo_app/items.html"

    def get_context_data(self, **kwargs):
        context = super(ItemForTestView, self).get_context_data(**kwargs)
        context['number_items'] = ItemForTest.objects.all().count()
        return context


class ItemDatabaseOneForTestView(TemplateView):
    template_name = "demo_app/items_database_by_queryset.html"

    def get_context_data(self, **kwargs):
        context = super(ItemDatabaseOneForTestView, self).get_context_data(**kwargs)
        name_database = get_database_depending_queryset_result(ItemForTest.objects.filter(name='Item1'))
        context['name_database'] = name_database
        context['number_items'] = ItemForTest.objects.all().count()
        return context


class ItemDatabaseTwoForTestView(TemplateView):
    template_name = "demo_app/items_database_by_queryset.html"

    def get_context_data(self, **kwargs):
        context = super(ItemDatabaseTwoForTestView, self).get_context_data(**kwargs)
        name_database = get_database_depending_queryset_result(ItemForTest.objects.filter(name='DB2_Item1'))
        context['name_database'] = name_database
        context['number_items'] = ItemForTest.objects.all().count()
        return context
