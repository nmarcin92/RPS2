import json
import random
import string

# from constants.resources import TOKENS_RES, MEASURES_RES
from flask import Flask, request, jsonify

from configuration import CONFIG
from persistence.mongo_database import Persistence
from rest.crossdomain import crossdomain
from rest.middleware import HTTPMethodOverrideMiddleware

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)


def generate_token():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(CONFIG.TOKEN_LENGTH))


# @app.route(MEASURES_RES, methods=['PUT'])
@app.route('/measures', methods=['PUT'])
def save_measure():
    token = request.get_json()['system_token']
    if Persistence.is_token_registered(token):
        buffer = request.get_json()['data']
        Persistence.save_measure(token, buffer)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


# @app.route(TOKENS_RES, methods=['PUT', 'OPTIONS'])
# @crossdomain(origin='*')
# @app.route(TOKENS_RES, methods=['PUT'])
@app.route('/tokens', methods=['PUT'])
def create_system_token():
    system_name = request.get_json()['system_name']
    tokens = Persistence.get_tokens()
    new_token = generate_token()
    while new_token in tokens:
        new_token = generate_token()
    Persistence.create_token(new_token, system_name)

    return jsonify({'generated_token': new_token})

#
# @app.route(TOKENS_RES + 's', methods=['GET', 'OPTIONS'])
# @crossdomain(origin='*')
# def get_system_names():
#     token = request.args.get('token')
#     sys_names = Persistence.get_system_names_by_token(token)
#     return jsonify({'names': sys_names})

def run_rest_server():
    import logging

# Log only in production mode.
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    app.run(port=8080)