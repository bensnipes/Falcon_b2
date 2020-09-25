import logging
import pathlib
import os
import sys


PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent  
# Package_root = C:\Users\Ben\Desktop\Falcon1_env\packages\regression_model\config

FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - "
    "%(funcName)s:%(lineno)d - %(message)s")


LOG_DIR = PACKAGE_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "ml_api.log"

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.DEBUG)
    return console_handler


def get_file_handler():
    file_handler = logging.FileHandler(LOG_FILE, "w")
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.INFO)
    return file_handler


def get_logger():
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger  




class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "this really needs to be changed"
    SERVER_PORT = 5000


class ProductionConfig(Config):
    DEBUG = False
    SERVER_PORT = os.environ.get("PORT",5000)


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True  

