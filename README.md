# Django SwitchDB

Django SwitchDB permit to change the database used. It use a Django Middleware and a 
specific database router.

# Usage 


## Change database according the host site.


If you will change database according to the host site, you must 
use settings.DATABASE_ALIAS_SELECTOR
 

```
DATABASE_ALIAS_CONFIGURATOR = {'test1.example.com:8000': 'default',
                               'test2.example.com:8000': 'other_database',
                              }
```


If you will use a different condition that the host site, you can 
define a callable and set the path import in settings.DATABASE_ALIAS_SELECTOR


```
DATABASE_ALIAS_SELECTOR = 'django_switchdb.db_selector.get_database_depending_on_request'
```

The effective choice is made by a Middleware (in middleware.py) SwitchDatabaseMiddleware.
SwitchDatabaseMiddleware use MiddlewareMixin so you can use it with django 1.8 or superior.


## Change database according to a queryset's result.

If you will change database according to the queryset's result, you must
use get_database_depending_queryset_result (in db_selector.py) and set settings.DATABASES_ALIAS_LIST.
That function take a query in argument (query). The query is execute in settings.DATABASES_ALIAS_LIST databases until
result exists.





