from datetime import datetime

from pymongo import MongoClient

from configuration import CONFIG


class Persistence(object):
    CLIENT = None
    DB = None

    @staticmethod
    def initialize():
        Persistence.CLIENT = MongoClient(CONFIG.MONGODB_SERVER_ADDR)
        Persistence.DB = Persistence.CLIENT.rps2

    @staticmethod
    def get_tokens():
        return [t['token'] for t in Persistence.DB.tokens.find()]

    @staticmethod
    def create_token(token, system_name):
        Persistence.DB.tokens.insert_one({
            'token': token,
            'system_name': system_name
        })

    @staticmethod
    def is_token_registered(token):
        return token in Persistence.get_tokens()

    @staticmethod
    def save_measure(token, buffer):
        resources = {}
        for data in buffer:
            timestamp = datetime.fromtimestamp(data['timestamp'])
            for type, measured in data['measured'].iteritems():
                if type not in resources:
                    resources[type] = []
                resources[type].append(
                        {'timestamp:': timestamp,
                         'measured:': measured})

        for type, measurements in resources.iteritems():
            collection_name = Persistence.get_collection_name(token, type)
            Persistence.DB[collection_name].insert_many(measurements)

    @staticmethod
    def get_system_name_by_token(token):
        system = Persistence.DB.tokens.find_one({
            'token': token
        })
        return system['system_name']

    @staticmethod
    def get_monitored_data(token, type, start_date, end_date):
        collection_name = Persistence.get_collection_name(token, type)
        collection = Persistence.DB[collection_name]
        if collection is not None:
            return {'data': [measure for measure in collection.find({'timestamp': {
                '$gt': start_date,
                '$lt': end_date
            }})]}
        else:
            return {}

    @classmethod
    def get_collection_name(cls, token, type):
        return token + '#' + type