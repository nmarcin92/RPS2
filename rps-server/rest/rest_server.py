import json
import random
import string

from constants.resources import TOKENS_RES, MEASURES_RES
from flask import Flask, request, jsonify

from persistence.mongo_database import Persistence
from rest.crossdomain import crossdomain
from rest.measures import save_measure, get_monitored_data
from rest.middleware import HTTPMethodOverrideMiddleware
from rest.tokens import get_system_name, create_system_token

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)


@app.route(TOKENS_RES, methods=['PUT', 'GET', 'OPTIONS'])
@crossdomain(origin='*')
def handle_tokens_request():
    if request.method == 'GET':
        return get_system_name()
    elif request.method == 'PUT':
        return create_system_token()


@app.route(MEASURES_RES, methods=['GET', 'PUT', 'OPTIONS'])
@crossdomain(origin='*')
def handle_measures_request():
    if request.method == 'GET':
        return get_monitored_data()
    elif request.method == 'PUT':
        return save_measure()


def run_rest_server():
    import logging

    # Log only in production mode.
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    app.run(port=8080)
