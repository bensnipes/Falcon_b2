import logging

import sys

from ...regression_model.config.config import LOG_DIR


# Multiple calls to logging.getLogger("someLogger") return a 
# reference to the same logger object. This is true not only 
# within the same module, but across modules as long as 
#it is within the same python interpreter process.

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -"
                                "%(funcName)s:%(lineno)d - %(message)s")
LOG_FILE = LOG_DIR / "ml_models.log"
logging.basicConfig(level=logging.DEBUG, format=FORMATTER, filemode="w")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)  
    return console_handler


def get_file_handler():
    file_handler = logging.FileHandler(LOG_FILE, "w")
    file_handler.setLevel(logging.DEBUG)
    return file_handler



def get_logger():
    logger = logging.getLogger()
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
  
    return logger