import pytest
from factiva.core import APIKeyUser
from factiva.helper import load_environment_value

FACTIVA_APIKEY = load_environment_value("FACTIVA_APIKEY")
DUMMY_KEY = 'abcd1234abcd1234abcd1234abcd1234'

# API Response sample with the most complete set of attributes
# {
#     "data": {
#         "id": "abcd1234abcd1234abcd1234abcd1234",
#         "attributes": {
#             "cnt_curr_ext": 1,
#             "current_downloaded_amount": 427567508,
#             "max_allowed_concurrent_extracts": 10,
#             "max_allowed_document_extracts": 2500000,
#             "max_allowed_extracts": 5,
#             "name": "Company Corp",
#             "products": "DNA",
#             "tot_document_extracts": 1595383,
#             "tot_extracts": 4,
#             "tot_subscriptions": 0,
#             "tot_topics": 0,
#             "licensed_company_ids": [
#                 4,
#                 3,
#                 1,
#                 5
#             ],
#             "enabled_company_identifiers": [
#                 {
#                     "id": 4,
#                     "name": "isin"
#                 },
#                 {
#                     "id": 3,
#                     "name": "cusip"
#                 },
#                 {
#                     "id": 1,
#                     "name": "sedol"
#                 },
#                 {
#                     "id": 5,
#                     "name": "ticker_exchange"
#                 }
#             ]
#         },
#         "type": "account_with_contract_limits"
#     }
# }



def check_apikeyuser_types(aku):
    aku = APIKeyUser(request_info=True)
    assert type(aku.api_key) == str
    assert type(aku.account_name) == str
    assert type(aku.active_products) == str
    assert type(aku.max_allowed_concurrent_extractions) == int
    assert type(aku.max_allowed_extracted_documents) == int
    assert type(aku.max_allowed_extractions) == int
    assert type(aku.remaining_documents) == int
    assert type(aku.remaining_extractions) == int
    assert type(aku.total_downloaded_bytes) == int
    assert type(aku.total_extracted_documents) == int
    assert type(aku.total_extractions) == int
    assert type(aku.total_stream_subscriptions) == int
    assert type(aku.total_stream_topics) == int
    assert type(aku.enabled_company_identifiers) == list

def test_apikeyuser_with_request_info():
    # Creates the object using the ENV variable and request the usage details to the API service
    aku = APIKeyUser(request_info=True)
    check_apikeyuser_types(aku)
    assert aku.api_key == FACTIVA_APIKEY
    assert len(aku.account_name) > 0
    assert len(aku.active_products) > 0

def test_apikeyuser_without_info():
    # Creates an empty object from the ENV variable with a value only for the api_key property
    aku = APIKeyUser()
    check_apikeyuser_types(aku)
    assert aku.api_key == FACTIVA_APIKEY
    assert len(aku.account_name) == 0
    assert len(aku.active_products) == 0

def test_user_with_parameter_and_info():
    # API Key is passed as a string and request_info=True
    aku = APIKeyUser(api_key=FACTIVA_APIKEY, request_info=True)
    check_apikeyuser_types(aku)
    assert aku.api_key == FACTIVA_APIKEY
    assert len(aku.account_name) > 0
    assert len(aku.active_products) > 0

# Creates an empty object from the provided string with a value only for the api_key property
def test_user_with_parameter_without_info():
    aku = APIKeyUser(DUMMY_KEY)
    check_apikeyuser_types(aku)
    assert aku.api_key == DUMMY_KEY
    assert aku.account_name == ''
    assert aku.active_products == ''

def test_invalid_key():
    # Creates an object from the provided string and request the usage details to the API service
    # The key is invalid and this should validate how the error is processed
    with pytest.raises(ValueError, match=r'Factiva API-Key does not exist or inactive.'):
        aku = APIKeyUser(DUMMY_KEY, request_info=True)

def test_invald_lenght_key():
    # Attempts to create an object with malformed keys. This requires assert the raised exception.
    with pytest.raises(ValueError, match=r'Factiva API-Key has the wrong length'):
        aku = APIKeyUser('abc')
