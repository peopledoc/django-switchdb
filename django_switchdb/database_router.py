

import threading
database_cfg = threading.local()


class SwitchDBRouter(object):
    def _get_database_name_in_local_thread_data(self):

        if hasattr(database_cfg, 'name_database'):
            return database_cfg.name_database
        else:
            return 'default'

    def db_for_read(self, model, **hints):
        return self._get_database_name_in_local_thread_data()

    def db_for_write(self, model, **hints):
        return self._get_database_name_in_local_thread_data()
