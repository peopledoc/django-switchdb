
from importlib import import_module

from django.conf import settings


from .database_router import database_cfg


class SwitchDatabaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        module_path, _, function_name = settings.DATABASE_SELECTOR.rpartition('.')
        try:
            function_for_select_database = getattr(import_module(module_path), function_name)
            database_cfg.name_database = function_for_select_database(request)
        except AttributeError:
            raise ImportError(settings.DATABASE_SELECTOR)

        response = self.get_response(request)

        del database_cfg.name_database

        return response
