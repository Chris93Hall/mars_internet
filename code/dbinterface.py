"""
dbinterface.py

The database contains two tables.
- queue
- cache

-------------------
 Queue table
-------------------
- url
- datetime_added
- reason_code

-------------------
Cache table
-------------------
- url
- datetime_cached
- reason_code
"""

import datetime
import psycopg2

class QueueInterface(object):
    def __init__(self):
        return

    def url_is_queued(self, url):
        return

    def get_queue_list(self, num_vals=-1):
        return

    def put_on_queue(self, url):
        return

class CacheInterface(object):
    def __init__(self):
        return

    def url_is_cached(self, url):
        return

    def get_cached_urls(self, num_vals=-1):
        return

class CachePromoter(object):
    def __init__(self):
        return

class DBInitializer(object):
    def __init__(self):
        return
