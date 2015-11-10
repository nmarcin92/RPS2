import ConfigParser


class Configuration(object):
    def __init__(self, filepath):
        config = ConfigParser.ConfigParser()
        config.read(filepath)

        self.CPU_MEASURE_INTERVAL = config.getfloat("CPUMeasure", "interval")
