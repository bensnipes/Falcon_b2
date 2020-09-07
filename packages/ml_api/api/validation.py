from marshmallow import Schema, fields

from marshmallow import ValidationError

import typing as t
import json

    
class InvalidInputError(Exception):
    """Invalid model input."""

    

class HouseDataRequestSchema(Schema):
    longitude = fields.Float()
    latitude = fields.Float()
    housing_median_age = fields.Float()
    total_rooms = fields.Float()
    total_bedrooms = fields.Float()
    population = fields.Float(allow_none=True)
    households = fields.Float(allow_none=True)
    median_income = fields.Float()
    median_house_value = fields.Float(allow_none=True)
    ocean_proximity = fields.Str()


def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    
    #remove input data rows with errors.

    indexes = errors.keys()
    #delete them in the reverse order so that you don't throw off subsequent indexes.

    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input



def validate_inputs(input_json):

    #check prediction inputs against schema.

    #set many=True to allow passing in a list
    schema = HouseDataRequestSchema(strict=True, many=True)
    input_data = json.loads(input_json)

    #convert syntax error field names(beginning with numbers)...ommitted in this version
    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors =exc.messages



    #convert syntax error field names back
    #this is a hack - never name your data
    # fields with numbers as the first letter...ommitted in this version
    if errors:
        validate_input = _filter_error_rows(
            errors=errors,
            validated_input= input_data
        )
    else:
        validate_input = input_data

    return validate_input, errors



