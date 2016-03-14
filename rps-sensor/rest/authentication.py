import requests

from utils.configuration import CONFIG
from utils.logger import LOGGER

TOKEN_START = '=== TOKEN START ==='
TOKEN_END = '==================='


class TokenNotFoundException(Exception):
    pass


def aquire_token():
    LOGGER.info('Trying to aquire token from server')
    token_file = open(CONFIG.TOKEN_FILE, 'w')
    req = requests.put(CONFIG.TOKENS_ADDR, json={'system_name': CONFIG.SYSTEM_NAME})
    if req.ok:
        LOGGER.info('Aquiring token from server succeeded')
        generated_token = req.json()['generated_token']
        token_file.write('\n'.join([TOKEN_START, generated_token, TOKEN_END]))
        return generated_token
    else:
        LOGGER.error('Failed to aquire token from server')
        raise TokenNotFoundException()


def obtain_system_token():
    LOGGER.info('Trying to read token from file: %s', CONFIG.TOKEN_FILE)
    token_file = open(CONFIG.TOKEN_FILE, 'r')
    file_content = token_file.read().splitlines()

    if len(file_content) >= 2 and file_content[0] == TOKEN_START and file_content[2] == TOKEN_END:
        LOGGER.info('Reading token from file succeeded')
        return file_content[1]
    else:
        LOGGER.warn('Reading token from file failed')
        return aquire_token()
