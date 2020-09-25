from flask import Flask

from ml_api.api.config import get_logger


_logger = get_logger()

def create_app(*, config_object) -> Flask:

    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)

    from ml_api.api.controller import prediction_app
    flask_app.register_blueprint(prediction_app)
    _logger.debug("Application instance created")


    return flask_app