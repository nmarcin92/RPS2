import logging

import requests
import time

from configuration import CONFIG
from measurers import cpu, memory, users

from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=format, filename='log.log', level=logging.INFO)
LOGGER = logging.getLogger('rps-sensor')


def initialize():
    LOGGER.info('Sensor module initialized successfully')


def send_buffer(data_buffer):
    data = {'send_timestamp': time.time(),
            'data': data_buffer
            }
    req = requests.post(CONFIG.SERVER_ADDR, json=data)
    if req.ok:
        LOGGER.info('Data pack sent')


def measure_loop():
    data_buffer = []

    while True:

        data = {'timestamp': time.time()}
        data['cpu'] = cpu.measure_cpu()
        data['memory'] = memory.measure_memory()

        data_buffer.append(data)

        if len(data_buffer) == CONFIG.BUFFER_SIZE:
            send_buffer(data_buffer)
            data_buffer = []


def main():
    initialize()
    measure_loop()


if __name__ == '__main__':
    main()