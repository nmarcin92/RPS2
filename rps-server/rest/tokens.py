import random
import string

from flask import request, jsonify

from configuration import CONFIG
from persistence.mongo_database import Persistence


def generate_token():
    return ''.join(
            random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(CONFIG.TOKEN_LENGTH))


def create_system_token():
    system_name = request.get_json()['system_name']
    tokens = Persistence.get_tokens()
    new_token = generate_token()
    while new_token in tokens:
        new_token = generate_token()
    Persistence.create_token(new_token, system_name)

    return jsonify({'generated_token': new_token})


def get_system_name():
    token = request.args.get('token')
    sys_name = Persistence.get_system_name_by_token(token)
    return jsonify({'name': sys_name})
