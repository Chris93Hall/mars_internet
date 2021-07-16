"""
flask_app.py

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
"""

import flask
from flask import request, jsonify

from dbinterface import CacheDBInterface

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/v1/hello_world', methods=['GET'])
def hello():
    return 'hello world'


@app.route('/api/v1/get_cache_state', methods=['GET'])
def get_cache_state():
    resp = {'url': 'google.com',
            'cache_state': 'CACHED'}
    return jsonify(resp)

app.run()

