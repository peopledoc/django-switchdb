
from django.conf.urls import url

from .views import ItemForTestView, ItemDatabaseOneForTestView, ItemDatabaseTwoForTestView


urlpatterns = [
    url(r'items_database_one', ItemDatabaseOneForTestView.as_view(), name='items_database_one'),
    url(r'items_database_two', ItemDatabaseTwoForTestView.as_view(), name='items_database_two'),
    url(r'items', ItemForTestView.as_view(), name='items'),
]
