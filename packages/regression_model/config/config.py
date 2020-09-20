import pathlib




PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "Datasets"
LOG_DIR = PACKAGE_ROOT / "ml_models.log"

#data
TESTING_DATA_FILE = DATASET_DIR / "test.csv"
TRAINING_DATA_FILE = DATASET_DIR / "train.csv"
TARGET = "median_house_value"

#variables
FEATURES = ["longitude", "latitude","median_income", "ocean_proximity","total_bedrooms","population","median_house_value","housing_median_age","total_rooms","households"]

CATEGORICAL_VARS = ["ocean_proximity"]
NUMERICAL_VARS_WITH_NA = ["total_bedrooms"]
NUMERICAL_LOG_VARS = ["latitude","housing_median_age","total_rooms","total_bedrooms","population","households", "median_income", "median_house_value"]
DROP_FEATURES = ["housing_median_age","total_rooms","total_bedrooms","population","households"]
NUMERICAL_VARS = ["latitude","housing_median_age","total_rooms","population","households", "median_income", "median_house_value","longitude"]

PIPELINE_NAME = "lasso_regression"
PIPELINE_SAVE_FILE =  f'{PIPELINE_NAME}_output_v'

ACCEPTABLE_MODEL_DIFFERENCE = 0.05





