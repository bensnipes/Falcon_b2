from sklearn.pipeline import Pipeline

import regression_model.preprocessors as pp

from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler
from regression_model.config import config
from regression_model.processing import features



price_pipe = Pipeline(
    [("categorical_imputer", pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),

    ("numerical_imputer", pp.NumericalImputer(variables=config.NUMERICAL_VARS_WITH_NA)),

    ("rare_label_encoder", pp.RareLabelCategoricalEncoder(tol=0.01, variables=config.CATEGORICAL_VARS)),

    ("categorical_encoder", pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),

    ("log_transformer", features.LogTransformer(variables=config.NUMERICAL_LOG_VARS)),

    ("drop_features", pp.DropUnnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)),

    ("scaler", MinMaxScaler()),

    ("linear_model", Lasso(alpha=0.005, random_state=0))])


