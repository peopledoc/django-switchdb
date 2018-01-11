
from django.conf import settings


def get_database_depending_on_request(request):
    return settings.DATABASE_CONFIGURATOR.get(request.get_host(), "default")
