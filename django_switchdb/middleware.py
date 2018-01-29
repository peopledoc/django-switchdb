
from importlib import import_module

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


from .database_router import database_cfg


class SwitchDatabaseMiddleware(MiddlewareMixin):

    def process_request(self, request):
        module_path, _, function_name = settings.DATABASE_SELECTOR.rpartition('.')
        try:
            function_for_select_database = getattr(import_module(module_path), function_name)
            database_cfg.name_database = function_for_select_database(request)
        except AttributeError:
            raise ImportError(settings.DATABASE_SELECTOR)

    def process_response(self, request, response):
        if hasattr(database_cfg, 'name_database'):
            del database_cfg.name_database
        return response
