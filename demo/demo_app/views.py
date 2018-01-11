# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from django.views.generic import TemplateView

from .models import ItemForTest


class ItemForTestView(TemplateView):
    template_name = "demo_app/items.html"

    def get_context_data(self, **kwargs):
        context = super(ItemForTestView, self).get_context_data(**kwargs)
        context['number_items'] = ItemForTest.objects.all().count()
        return context
