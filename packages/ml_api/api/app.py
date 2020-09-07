from flask import Flask
import logging
from ml_api.api import config

_logger = config.get_logger()


def create_app(config_object) -> Flask:
    # create a flask app instance.
    flask_app = Flask("ml_api")
    flask_app.config.from_object(config_object)

    # import blueprints
    from ml_api.api.controller import prediction_app
    flask_app.register_blueprint(prediction_app)

    return flask_app