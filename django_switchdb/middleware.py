
from importlib import import_module

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


from .database_router import database_cfg


class SwitchDatabaseMiddleware(MiddlewareMixin):

    def process_request(self, request):
        module_path, _, function_name = settings.DATABASE_ALIAS_SELECTOR.rpartition('.')
        try:
            function_for_select_database = getattr(import_module(module_path), function_name)
            database_cfg.alias_database = function_for_select_database(request)
        except AttributeError:
            raise ImportError(settings.DATABASE_ALIAS_SELECTOR)

    def process_response(self, request, response):
        if hasattr(database_cfg, 'alias_database'):
            del database_cfg.alias_database
        return response
