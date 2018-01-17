# Django SwitchDB

Django SwitchDB permit to change the database used. It use a Django Middleware and a 
specific database router.

# Usage 

If you will change database according to the host site, you must 
use settings.DATABASE_SELECTOR
 

```
DATABASE_CONFIGURATOR = {'test1.example.com:8000': 'default',
                         'test2.example.com:8000': 'other_database',
                         }
```


If you will use a different condition that the host site, you can 
define a callable and set the path import in settings.DATABASE_SELECTOR


```
DATABASE_SELECTOR = 'django_switchdb.db_selector.get_database_depending_on_request'
```
