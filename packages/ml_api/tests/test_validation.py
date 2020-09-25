import json
from ...regression_model.config import config

from ...regression_model.processing.data_management import load_dataset


def test_prediction_endpoint_validation_200(flask_test_client):
    #Given
    #Load the test data from the regression model package
    # Data versions to get confused by not spreading it 
    # across packages.

    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    post_json = test_data.to_json(orient="records")

    #when 
    response = flask_test_client.post("/v1/predict/regression", json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)

    #check correct number of errors removed
    assert len(response_json.get("predictions")) + len(response_json.get("errors")) == len(test_data)


    