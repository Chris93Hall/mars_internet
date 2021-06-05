"""
dbinterface.py

-------------------
Cache table
-------------------
- url (string)
- time_cached (timestamp)
- time_last_accessed (timestamp)
- reason_code (int)
  - 0 (autocached)
  - 1 (manually saved) 
"""

import datetime
import os
import time
import sqlite3

class DBInterface(object):
    def __init__(self, filepath):
        filepath = os.path.expandvars(filepath)
        if not os.path.isfile(filepath):
            raise Exception('File does not exist: {}'.format(filepath))

        self.conn = sqlite3.connect(filepath)
        self.cursor = self.conn.cursor()
        return

    def close(self):
        self.cursor.close()
        self.conn.close()

class CacheDBInterface(DBInterface):
    def __init__(self, filepath):
        super().__init__(filepath)
        return

    def get_all_data(self):
        self.cursor.execute("""SELECT * from cache;""")
        rows = self.cursor.fetchall()
        return rows

    def url_is_cached(self, url, queue_dur=480):
        queue_start_time = time.time() - queue_dur
        cmd = "select url from cache where url='{}' and time_cached < {};".format(url, queue_start_time)
        self.cursor.execute(cmd)
        testval = self.cursor.fetchone()
        if testval:
            return True
        return False

    def url_is_queued(self, url, queue_dur=480):
        queue_start_time = time.time() - queue_dur
        cmd = "select url from cache where url='{}' and time_cached > {};".format(url, queue_start_time)
        self.cursor.execute(cmd)
        testval = self.cursor.fetchone()
        if testval:
            return True
        return False

    def url_in_table(self, url):
        cmd = "select url from cache where url='{}';".format(url)
        self.cursor.execute(cmd)
        testval = self.cursor.fetchone()
        if testval:
            return True
        return False

    def get_cache_state(self, url, queue_dur=480):
        """
        Returns either 'NONE', 'QUEUED', or 'CACHED'

        TODO
        """
        return

    def add_url_to_cache(self, url, reason_code=0):
        cmd = "INSERT INTO cache VALUES ('{}', {}, {}, {});".format(url, time.time(), 'null', reason_code)
        self.cursor.execute(cmd)
        self.conn.commit()
        return

    def attempt_url_access(self, url):
        """
        Return True if URL is on cache and queue time has elapsed
        Will update the time_last_accessed column in the database
        """
        if not self.url_is_cached(url):
            return False
        current_time = time.time()
        cmd = "UPDATE cache SET time_last_accessed={} where url='{}';".format(current_time, url)
        self.cursor.execute(cmd)
        self.conn.commit()
        return True

    def get_cached_urls(self, queue_dur=480, num_vals=-1):
        """
        Get list of all urls that are in the table and have completed
        the queue duration

        Does not update time_last_accessed column
        """
        current_time = time.time()
        queue_start_time = current_time - queue_dur
        cmd = "SELECT * from cache where time_cached < {} limit {}".format(queue_start_time, num_vals)
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        return rows

    def get_queued_urls(self):
        return

class DBInitializer(DBInterface):
    def __init__(self, filepath):
        super().__init__(filepath)
        return

    def build_tables(self):
        """
        Build tables that need to exist.
        Will be a NOOP for tables that already exist.
        """
        # check if table already exists
        if not self.check_table_exists('cache')
            # build cache table
            self.cursor.execute("""CREATE TABLE cache (url char(256), time_cached timestamp, time_last_accessed timestamp, reason_code int(255));""")
        self.conn.commit()
        return

    def check_table_exists(self, table_name):
        cmd = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        self.cursor.execute(cmd)
        res = self.cursor.fetchone()
        if not res:
            return True
        return False

