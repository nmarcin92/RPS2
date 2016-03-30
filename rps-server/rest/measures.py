import json

from flask import request, jsonify

from persistence.mongo_database import Persistence


def save_measure():
    token = request.get_json()['system_token']
    if Persistence.is_token_registered(token):
        buffer = request.get_json()['data']
        Persistence.save_measure(token, buffer)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


def get_monitored_data():
    token = request.args.get('token')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    type = request.args.get('type')

    return jsonify(Persistence.get_monitored_data(token, type, start_date, end_date))