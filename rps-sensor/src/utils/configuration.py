import ConfigParser
import os


class Configuration(object):
    def __init__(self, filepath):
        config = ConfigParser.ConfigParser()
        config.read(filepath)

        self.CPU_MEASURE_INTERVAL = config.getfloat('CPUMeasure', 'interval')

        self.BUFFER_SIZE = config.getint('MeasureConfig', 'buffer_size')
        self.SERVER_ADDR = config.get('MeasureConfig', 'server_address') + ':' + config.get('MeasureConfig', 'server_port')
        self.SLEEP_TIME = config.getfloat('MeasureConfig', 'sleep_time')

        self.TOKEN_FILE = os.path.join(ROOT_DIR, config.get('Authentication', 'token_file'))
        self.SYSTEM_NAME = config.get('Authentication', 'system_name')


ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))
CONFIG = Configuration(os.path.join(ROOT_DIR, 'conf.ini'))