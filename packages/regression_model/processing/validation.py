from ...regression_model.config import config
import pandas as pd



def validated_inputs(input_data: pd.DataFrame) -> pd.DataFrame:

    validated_data = input_data.copy()

    #check for numerical variables with NA not seen during training
    if input_data[config.NUMERICAL_VARS_WITH_NA].isnull().any().any():
        validated_data = validated_data.dropna(axis=0, subset=config.NUMERICAL_VARS_WITH_NA)

    
    #check for categorical variables with NA not seen during training
    
    if input_data[config.CATEGORICAL_VARS].isnull().any().any():
        validated_data = validated_data.dropna(axis=0, subset=config.CATEGORICAL_VARS)


    #check for values less than or equal to 0 for the log transformed variables
    if (input_data[config.NUMERICAL_LOG_VARS] <= 0).any().any():
        vars_with_neg_values = config.NUMERICAL_LOG_VARS[(input_data[config.NUMERICAL_LOG_VARS] <= 0).any()]
        validated_data = validated_data[validated_data[vars_with_neg_values] > 0]

    return validated_data
