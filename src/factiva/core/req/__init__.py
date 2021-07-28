"""
    Module to handle the API and other requests
"""
import requests, json
from .. import const


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
