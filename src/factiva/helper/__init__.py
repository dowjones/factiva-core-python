import os
import requests
import json
from factiva.core import const


def load_environment_value(config_key):
    tmp_val = os.getenv(config_key, None)
    if tmp_val is None:
        raise Exception("Environment Variable {} not found!".format(config_key))
    return tmp_val


def mask_string(raw_str, right_padding=4):
    return raw_str[-right_padding:].rjust(len(raw_str), '*')


def api_send_request(method='GET', endpoint_url=const.API_HOST, headers=None, payload=None, qs_params=None):

    if headers is None:
        raise ValueError('Heders for Factiva requests cannot be empty')

    if type(headers) is not dict:
        raise ValueError('Unexpected headers value')

    try:
        if method == 'GET':
            if qs_params is not None:
                if type(qs_params) is not dict:
                    raise ValueError('Unexpected qs_params value')
            response = requests.get(endpoint_url, headers=headers, params=qs_params)

        elif method == 'POST':
            if payload is not None:
                if type(payload) == dict:
                    payload_str = json.dumps(payload)
                elif type(payload) == str:
                    payload_str = payload
                else:
                    raise ValueError('Unexpected payload value')
            response = requests.post(endpoint_url, headers=headers, data=payload_str)

        else:
            raise ValueError('Unexpected method value')

    except Exception:
        raise RuntimeError('API Request failed. Unspecified Error.')

    return response
