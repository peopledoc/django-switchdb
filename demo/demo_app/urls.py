
from django.conf.urls import url

from .views import ItemForTestView


urlpatterns = [
    url(r'items', ItemForTestView.as_view(), name='items'),
]
