from collections import namedtuple

from data import MeasureData


class MemoryData(MeasureData):
    def __init__(self):
        self.virtual = namedtuple('Float', ['total', 'available'])
        self.swap = namedtuple('Float', ['total', 'available'])
