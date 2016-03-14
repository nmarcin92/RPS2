import time

from measurers import cpu, memory
from rest.authentication import obtain_system_token
from rest.measuring import send_buffer
from utils.configuration import CONFIG
from utils.logger import LOGGER
from utils.session import SessionInfo

SESSION_INFO = SessionInfo()


def initialize():
    LOGGER.info('Initializing sensor module')
    SESSION_INFO.TOKEN = obtain_system_token()
    LOGGER.info('Sensor module initialized successfully')


def measure_loop():
    data_buffer = []

    while True:

        data = {'timestamp': time.time()}
        data['cpu'] = cpu.measure_cpu()
        data['memory'] = memory.measure_memory()

        data_buffer.append(data)

        if len(data_buffer) == CONFIG.BUFFER_SIZE:
            send_buffer(data_buffer, SESSION_INFO.TOKEN)
            data_buffer = []


def main():
    initialize()
    measure_loop()


if __name__ == '__main__':
    main()
