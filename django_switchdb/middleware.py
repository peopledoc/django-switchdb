
import threading
from importlib import import_module

from django.conf import settings


database_cfg = threading.local()


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


class DatabaseRouter(object):
    def _get_database_name_in_local_thread_data(self):

        if hasattr(database_cfg, 'name_database'):
            return database_cfg.name_database
        else:
            return 'default'

    def db_for_read(self, model, **hints):
        return self._get_database_name_in_local_thread_data()

    def db_for_write(self, model, **hints):
        return self._get_database_name_in_local_thread_data()
