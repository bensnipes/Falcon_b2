from flask import Blueprint, request, jsonify

from regression_model.predict import make_prediction
from api import __version__ as api_version
from regression_model import __version__ as _version

from api.validation import validate_inputs


from api.config import get_logger

_logger = get_logger()


prediction_app = Blueprint("prediction_app", __name__)

@prediction_app.route("/health", methods=["GET"])
def health():
    if request.method == "GET":
        _logger.info("Health status ok")
        return "Keep it Up Ben"



@prediction_app.route("/version", methods=["GET"])
def version():
    if request.method == "GET":
        return jsonify({"model_version": _version,"api_version": api_version})



@prediction_app.route("/v1/predict/regression", methods=["POST"])
def predict():
    if request.method == "POST":
        json_data = request.get_json()
        _logger.info(f"Inputs: {json_data}")

        input_data, errors = validate_inputs(input_json=json_data)

        result = make_prediction(input_data=json_data)
        _logger.info(f"Outputs: {result}")

        predictions = result.get("predictions")
        version = result.get("version")

         # step5: Return the response as JSON
        return jsonify({"predictions": predictions, "version": version, "errors": errors})
                       

    # Have left the last endpoint classifier.

        