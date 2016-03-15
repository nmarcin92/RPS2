from datetime import datetime

from pymongo import MongoClient

from configuration import CONFIG


class Persistence(object):
    CLIENT = None
    METADATA_DB = None

    @staticmethod
    def initialize():
        Persistence.CLIENT = MongoClient(CONFIG.MONGODB_SERVER_ADDR)
        Persistence.METADATA_DB = Persistence.CLIENT.rps2

    @staticmethod
    def get_tokens():
        return [t['token'] for t in Persistence.METADATA_DB.tokens.find()]

    @staticmethod
    def create_token(token, system_name):
        Persistence.METADATA_DB.tokens.insert_one({
            'token': token,
            'system_name': system_name
        })

    @staticmethod
    def is_token_registered(token):
        return token in Persistence.get_tokens()

    @staticmethod
    def save_measure(token, buffer):
        db = Persistence.CLIENT[token]
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
            db[type].insert_many(measurements)
