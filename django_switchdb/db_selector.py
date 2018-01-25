
from django.conf import settings

from .database_router import database_cfg


def get_database_depending_on_request(request):
    return settings.DATABASE_CONFIGURATOR.get(request.get_host(), "default")


def get_database_depending_queryset_result(query):
    for name_database in settings.DATABASES_LIST:
        if query.using(name_database).exists():
            database_cfg.name_database = name_database
            return name_database
    return None
