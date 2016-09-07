import logging
import os

import sys

from configuration import ROOT_DIR

formatter = logging.Formatter('%(asctime)-15s [%(levelname)-5.5s] %(message)s')
LOGGER = logging.getLogger('rps-sensor')
LOGGER.setLevel(logging.INFO)

fileHandler = logging.FileHandler(os.path.join(ROOT_DIR, 'log.log'))
fileHandler.setFormatter(formatter)
LOGGER.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(formatter)
LOGGER.addHandler(consoleHandler)