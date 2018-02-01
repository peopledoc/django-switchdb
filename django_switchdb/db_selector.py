
from django.conf import settings

from .database_router import database_cfg


def get_database_depending_on_request(request):
    return settings.DATABASE_ALIAS_CONFIGURATOR.get(request.get_host(), "default")


def get_database_depending_queryset_result(query):
    for alias_database in settings.DATABASES_ALIAS_LIST:
        if query.using(alias_database).exists():
            database_cfg.alias_database = alias_database
            return alias_database
    return None
