"""
flask_app.py

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
"""

import os

import flask
from flask import request, jsonify

from dbinterface import CacheDBInterface
from delay_keeper import DelayKeeper

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/v1/hello_world', methods=['GET'])
def hello():
    return 'hello world'


@app.route('/api/v1/get_cache_state', methods=['GET'])
def get_cache_state():
    """
    Expect data to be in the following format:
    {'urls': ['url1', 'url2', 'url3']}

    Response will be:
    {'urls': [('url1', 'CACHED', ('url2', 'QUEUED'), ('url3', 'NONE')]}
    """
    data = request.get_json()
    
    urls_list = data['urls']
    url_status_list = []

    # It would be nice if we could abstract away any database type specific
    # things to a single common interface.
    db_path = os.path.expandvars('$MARSNET_ROOT/db/marsnet.db')
    dbutil = CacheDBInterface(db_path)
    with dbutil as db:
        for url in urls_list:
            status_tmp = db.get_cache_state(url) # Returns CACHED, QUEUED, or NONE
            url_status_list.append((url, status_tmp))

    resp = {'urls': url_status_list}
    return jsonify(resp)

@app.route('/api/v1/add_to_cache', methods=['POST'])
def add_to_cache():
    """
    Expect post data to be of the following format:
    {'urls': [('url1', reason_code), ('url2', reason_code), ('url3', reason_code)]}
    """
    data = request.get_json()
    urls_list = data['urls']
    with dbutil as db:
        for url, reason_code in urls_list:
            db.add_url_to_cache(url, reason_code)    
    return

@app.route('/api/v1/set_delay', methods=['POST'])
def set_delay():
    """
    Data should come in the following format:
    {'delay': 480}

    Delay given in seconds
    """
    data = request.get_json()
    delay = data['delay']
    DelayKeeper.set_delay(delay)
    return

@app.route('/api/v1/get_delay', methods=['GET'])
def get_delay():
    delay = DelayKeeper.get_delay()
    resp = {'delay': delay}
    return jsonify(resp)

app.run()

