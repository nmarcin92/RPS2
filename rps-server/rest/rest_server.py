import json
import random
import string

from constants.resources import TOKENS_RES, MEASURES_RES
from flask import Flask, request, jsonify

from configuration import CONFIG
from persistence.mongo_database import Persistence

app = Flask(__name__)


def generate_token():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(CONFIG.TOKEN_LENGTH))


@app.route(MEASURES_RES, methods=['PUT'])
def save_measure():
    token = request.get_json()['system_token']
    if Persistence.is_token_registered(token):
        buffer = request.get_json()['data']
        Persistence.save_measure(token, buffer)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route(TOKENS_RES, methods=['PUT'])
def create_system_token():
    system_name = request.get_json()['system_name']
    tokens = Persistence.get_tokens()
    new_token = generate_token()
    while new_token in tokens:
        new_token = generate_token()
    Persistence.create_token(new_token, system_name)

    return jsonify({'generated_token': new_token})


def run_rest_server():
    app.run(port=8080)