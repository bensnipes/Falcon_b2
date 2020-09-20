import numpy as np
import pandas as pd
import typing as t

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model.processing.validation import validated_inputs
from regression_model.config import logging_config
from regression_model import __version__ as _version

_logger = logging_config.get_logger()



pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:

    data = pd.DataFrame(input_data)
    # remember to include the evaluate
    validated_data = validated_inputs(input_data=data)
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = prediction
    
    results = {"predictions": output,'version': _version}

    _logger.debug(
        f"Making predictions with model version: {_version}"
        f"Inputs: {validated_data}"
        f"Predictions: {output}"
    )
 
    return results




    
