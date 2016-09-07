import ConfigParser


class Configuration(object):
    def __init__(self, filepath):
        config = ConfigParser.ConfigParser()
        config.readfp(filepath)

        self.MONGODB_SERVER_ADDR = config.get('MongoDB', 'dbserv_address') + ':' + config.get('MongoDB', 'dbserv_port')
        self.TOKEN_LENGTH = config.getint('Auth', 'token_length')

CONFIG = Configuration('conf.ini')