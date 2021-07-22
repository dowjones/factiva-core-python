import pytest
from factiva.core import UserKey
from factiva.helper import load_environment_value

FACTIVA_USERKEY = load_environment_value("FACTIVA_USERKEY")
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


def check_UserKey_types(aku):
    aku = UserKey(stats=True)
    assert type(aku.user_key) == str
    assert type(aku.cloud_token) == dict
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
    assert type(aku.total_stream_instances) == int
    assert type(aku.total_stream_subscriptions) == int
    assert type(aku.enabled_company_identifiers) == list


def test_UserKey_with_stats():
    # Creates the object using the ENV variable and request the usage details to the API service
    aku = UserKey(stats=True)
    check_UserKey_types(aku)
    assert aku.user_key == FACTIVA_USERKEY
    assert len(aku.account_name) > 0
    assert len(aku.active_products) > 0


def test_UserKey_without_stats():
    # Creates an empty object from the ENV variable with a value only for the user_key property
    aku = UserKey()
    check_UserKey_types(aku)
    assert aku.user_key == FACTIVA_USERKEY
    assert len(aku.account_name) == 0
    assert len(aku.active_products) == 0


def test_user_with_parameter_and_stats():
    # API Key is passed as a string and stats=True
    aku = UserKey(user_key=FACTIVA_USERKEY, stats=True)
    check_UserKey_types(aku)
    assert aku.user_key == FACTIVA_USERKEY
    assert len(aku.account_name) > 0
    assert len(aku.active_products) > 0


# Creates an empty object from the provided string with a value only for the user_key property
def test_user_with_parameter_without_stats():
    u = UserKey(DUMMY_KEY)
    check_UserKey_types(u)
    assert u.user_key == DUMMY_KEY
    assert u.account_name == ''
    assert u.active_products == ''


def test_invalid_key():
    # Creates an object from the provided string and request the usage details to the API service
    # The key is invalid and this should validate how the error is processed
    with pytest.raises(ValueError, match=r'Factiva User-Key does not exist or inactive.'):
        u = UserKey(DUMMY_KEY, stats=True)
        assert u.account_name != ''


def test_invald_lenght_key():
    # Attempts to create an object with malformed keys. This requires assert the raised exception.
    with pytest.raises(ValueError, match=r'Factiva User-Key has the wrong length'):
        u = UserKey('abc')
        assert u.account_name != ''
