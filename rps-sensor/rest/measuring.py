import time

import requests

from utils.configuration import CONFIG
from utils.logger import LOGGER


def send_buffer(data_buffer, token):
    data = {'system_token': token,
            'send_timestamp': time.time(),
            'data': data_buffer
            }
    req = requests.post(CONFIG.SERVER_ADDR, json=data)
    if req.ok:
        LOGGER.info('Data pack sent')