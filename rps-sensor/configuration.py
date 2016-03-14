import ConfigParser


class Configuration(object):
    def __init__(self, filepath):
        config = ConfigParser.ConfigParser()
        config.read(filepath)

        self.CPU_MEASURE_INTERVAL = config.getfloat('CPUMeasure', 'interval')

        self.BUFFER_SIZE = config.getint('MeasureConfig', 'buffer_size')
        self.SERVER_ADDR = config.get('MeasureConfig', 'server_address') + ':' + config.get('MeasureConfig', 'server_port')
        self.SLEEP_TIME = config.getint('MeasureConfig', 'sleep_time')


CONFIG = Configuration('conf.ini')