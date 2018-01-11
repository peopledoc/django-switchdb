# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ItemForTestApiView


urlpatterns = [
    url(r'items', ItemForTestApiView.as_view(), name='api_items'),
]
