import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset
from regression_model.config import logging_config
from regression_model import __version__ as _version


_logger = logging_config.get_logger()




def test_make_single_prediction():

    #Given
    test_data = load_dataset(file_name="test.csv")
    single_test_json = test_data

    #When
    subject = make_prediction(input_data = single_test_json)
    return subject
    print(subject)


    #Then
    assert subject is not None
    assert isinstance(subject.get("predictions")[0], float)
    assert len(subject.get("predictions")) == 472677
    assert len(test_data) == 2045
    

    
    
    _logger.info(
        f"Predictions: {subject}"
        f"Making predictions with model versioned: {_version}")