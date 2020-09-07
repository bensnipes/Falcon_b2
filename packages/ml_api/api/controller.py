from flask import Blueprint, request, jsonify

from ml_api.api.config import get_logger
from regression_model import __version__ as _version

from regression_model.predict import make_prediction

from ml_api.api.validation import validate_inputs

from ml_api.api import __version__ as api_version


_logger = get_logger()

prediction_app = Blueprint("prediction_app", __name__)

@prediction_app.route("/health", methods=["GET"])
def health():
    if request.method == "GET":
        _logger.info("health status OK")
        return "ok"


@prediction_app.route("/version", methods=["GET"])
def version():
    if request.method == "GET":
        return jsonify({"model_version": _version,"api_version": api_version})




@prediction_app.route("/v1/predict/regression", methods=["POST"])
def predict():
    if request.method == "POST":
        # step1: Extract POST data from request body as JSON.

        json_data = request.get_json()
        _logger.info(f"inputs: {json_data}")

        # step2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_json=json_data)

        # step3: Model Prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f"Outputs:{result}")

        # step4: Convert numpy ndarray to list
        predictions = result.get("predictions").tolist()
        version = result.get("version")

        # step5: Return the response as JSON
        return jsonify({"predictions": predictions, "version": version, "errors": errors})
                       

    # Have left the last endpoint classifier.

        
        