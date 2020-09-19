import math

import pytest

import pandas as pd


from regression_model.config import config as model_config
from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


@pytest.mark.differential
def test_model_prediction_differential(*, save_file="test_data_predictions.csv"):


# This test compares the prediction result similarity of the 
# current model with the previous model's results.

    #Given
    previous_model_df = pd.read_csv(f'{model_config.PACKAGE_ROOT}/' f'regression_model/config/Datasets/{save_file}')
    previous_model_predictions = previous_model_df.predictions.values
    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    multiple_test_json = test_data[99:600]

    # When 
    response = make_prediction(input_data=multiple_test_json)
    current_model_predictions = response.get("predictions")

    assert len(previous_model_predictions) == len(current_model_predictions)

    # Perform the differential test
    for previous_value, current_value in zip(previous_model_predictions,current_model_predictions):

        # convert numpy float64 to python float
        previous_value = previous_value.item()
        current_value = current_value.item()

        # rel_tol is the relative tolerance - it is the maximum allowed

        assert math.isclose(previous_value, current_value, rel_tol=config.ACCEPTABLE_MODEL_DIFFERENCE)





