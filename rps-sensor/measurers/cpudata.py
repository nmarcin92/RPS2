from collections import namedtuple

from data import MeasureData


class CpuData(MeasureData):
    def __init__(self):
        self.usage = ()
        self.cpu_count = 0
        self.times = namedtuple('float', ['user', 'sys', 'idle'])
