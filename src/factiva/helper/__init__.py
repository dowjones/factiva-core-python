"""Implement different helper functions."""
import os
import json
import requests
from factiva.core import const


def load_environment_value(config_key):
    """Obtain a environmental variable."""
    tmp_val = os.getenv(config_key, None)
    if tmp_val is None:
        raise Exception("Environment Variable {} not found!".format(config_key))
    return tmp_val


def mask_string(raw_str, right_padding=4):
    """Mask a string with a default value of 4."""
    return raw_str[-right_padding:].rjust(len(raw_str), '*')


def send_get_request(endpoint_url=const.API_HOST, headers=None, qs_params=None):
    """Send get request."""
    if (qs_params is not None) and (not isinstance(qs_params, dict)):
        raise ValueError('Unexpected qs_params value')
    return requests.get(endpoint_url, headers=headers, params=qs_params)


def send_post_request(endpoint_url=const.API_HOST, headers=None, payload=None):
    """Send post request."""
    if payload is not None:
        if isinstance(payload, dict):
            payload_str = json.dumps(payload)
        elif isinstance(payload, str):
            payload_str = payload
        else:
            raise ValueError('Unexpected payload value')
        return requests.post(endpoint_url, headers=headers, data=payload_str)

    return requests.post(endpoint_url, headers=headers)


def api_send_request(method='GET', endpoint_url=const.API_HOST, headers=None, payload=None, qs_params=None):
    """Send a generic request to a certain API end point."""
    if headers is None:
        raise ValueError('Heders for Factiva requests cannot be empty')

    if not isinstance(headers, dict):
        raise ValueError('Unexpected headers value')

    try:
        if method == 'GET':
            response = send_get_request(endpoint_url=endpoint_url, headers=headers, qs_params=qs_params)

        elif method == 'POST':
            response = send_post_request(endpoint_url=endpoint_url, headers=headers, payload=payload)

        elif method == 'DELETE':
            response = requests.delete(endpoint_url, headers=headers)

        else:
            raise ValueError('Unexpected method value')

    except Exception:
        raise RuntimeError('API Request failed. Unspecified Error.')

    return response


def validate_type(var_to_validate, expected_type, error_message):
    """Validate a given type."""
    if not isinstance(var_to_validate, expected_type):
        raise ValueError(error_message)


def flatten_dict(multi_level_dict):
    """Flatten a dictionary."""
    flattened_dict = {}
    for entry in multi_level_dict:
        if isinstance(multi_level_dict[entry], dict):
            new_elements = flatten_dict(multi_level_dict[entry])
            flattened_dict.update(new_elements)
        else:
            flattened_dict[entry] = multi_level_dict[entry]

    return flattened_dict


def load_generic_env_variable(variable, env_var):
    """Load generic env variable."""
    if not variable:
        try:
            return load_environment_value(f'{env_var}')
        except Exception:
            return variable

    return variable
