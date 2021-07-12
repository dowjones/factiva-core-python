import pytest

from factiva.core import StreamUser
from factiva.helper import load_environment_value

FACTIVA_APIKEY = load_environment_value("FACTIVA_APIKEY")
FACTIVA_CLIENT_EMAIL = load_environment_value("FACTIVA_CLIENT_EMAIL")
DUMMY_KEY = 'abcd1234abcd1234abcd1234abcd1234'

def check_apikeyuser_types(su):
    su = StreamUser(request_info=True)
    assert type(su.api_key) == str
    assert type(su.account_name) == str
    assert type(su.active_products) == str
    assert type(su.max_allowed_concurrent_extractions) == int
    assert type(su.max_allowed_extracted_documents) == int
    assert type(su.max_allowed_extractions) == int
    assert type(su.remaining_documents) == int
    assert type(su.remaining_extractions) == int
    assert type(su.total_downloaded_bytes) == int
    assert type(su.total_extracted_documents) == int
    assert type(su.total_extractions) == int
    assert type(su.total_stream_subscriptions) == int
    assert type(su.total_stream_topics) == int
    assert type(su.enabled_company_identifiers) == list

def test_apikeyuser_with_request_info():
    # Creates the object using the ENV variable and request the usage details to the API service
    su = StreamUser(request_info=True)
    check_apikeyuser_types(su)
    assert su.api_key == FACTIVA_APIKEY
    assert len(su.account_name) > 0
    assert len(su.active_products) > 0

def test_apikeyuser_without_info():
    # Creates an empty object from the ENV variable with a value only for the api_key property
    su = StreamUser()
    check_apikeyuser_types(su)
    assert su.api_key == FACTIVA_APIKEY
    assert len(su.account_name) == 0
    assert len(su.active_products) == 0

def test_user_with_parameter_and_info():
    # API Key is passed as a string and request_info=True
    su = StreamUser(api_key=FACTIVA_APIKEY, request_info=True)
    check_apikeyuser_types(su)
    assert su.api_key == FACTIVA_APIKEY
    assert len(su.account_name) > 0
    assert len(su.active_products) > 0

# Creates an empty object from the provided string with a value only for the api_key property
def test_user_with_parameter_without_info():
    su = StreamUser(DUMMY_KEY)
    check_apikeyuser_types(su)
    assert su.api_key == DUMMY_KEY
    assert su.account_name == ''
    assert su.active_products == ''

def test_invalid_key():
    # Creates an object from the provided string and request the usage details to the API service
    # The key is invalid and this should validate how the error is processed
    with pytest.raises(ValueError, match=r'Factiva API-Key does not exist or inactive.'):
        StreamUser(DUMMY_KEY, request_info=True)

def test_invald_lenght_key():
    # Attempts to create an object with malformed keys. This requires assert the raised exception.
    with pytest.raises(ValueError, match=r'Factiva API-Key has the wrong length'):
        StreamUser('abc')

def test_get_credentials():
    su = StreamUser(api_key=FACTIVA_APIKEY)
    credentials = su.fetch_credentials()
    assert credentials != None
    assert isinstance(credentials, object)
    assert credentials['client_email'] == FACTIVA_CLIENT_EMAIL

def test_credentials_project_id():
    su = StreamUser(api_key=FACTIVA_APIKEY)
    credentials = su.fetch_credentials()
    assert credentials != None
    assert len(credentials['project_id']) >= 3
    assert credentials['client_email'] == FACTIVA_CLIENT_EMAIL

def test_credentials_client_id():
    su = StreamUser(api_key=FACTIVA_APIKEY)
    credentials = su.fetch_credentials()
    assert credentials != None
    assert credentials['client_email'] == FACTIVA_CLIENT_EMAIL


# TODO: When possible, define a method that consumes a fixed (reliable) authenticated resource.
