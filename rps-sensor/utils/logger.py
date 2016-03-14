import logging
import os

from utils.configuration import ROOT_DIR

format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=format, filename=os.path.join(ROOT_DIR, 'log.log'), level=logging.INFO)
LOGGER = logging.getLogger('rps-sensor')