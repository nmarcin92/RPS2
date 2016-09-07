import time

import requests
from constants.resources import MEASURES_RES

from ..utils.configuration import CONFIG
from ..utils.logger import LOGGER


def send_buffer(data_buffer, token):
    data = {'system_token': token,
            'send_timestamp': time.time(),
            'data': data_buffer
            }
    req = requests.put(CONFIG.SERVER_ADDR + MEASURES_RES, json=data)
    if req.ok:
        LOGGER.info('Data pack sent')