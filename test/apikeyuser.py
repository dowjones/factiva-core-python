from factiva.core import APIKeyUser
from factiva.helper import load_environment_value


def check_apikeyuser_types(aku_obj):
    assert type(aku_obj.api_key) == str
    assert type(aku_obj.account_name) == str
    assert type(aku_obj.active_products) == str
    assert type(aku_obj.max_allowed_concurrent_extractions) == int
    assert type(aku_obj.max_allowed_extracted_documents) == int
    assert type(aku_obj.max_allowed_extractions) == int
    assert type(aku_obj.remaining_documents) == int
    assert type(aku_obj.remaining_extractions) == int
    assert type(aku_obj.total_downloaded_bytes) == int
    assert type(aku_obj.total_extracted_documents) == int
    assert type(aku_obj.total_extractions) == int
    assert type(aku_obj.total_stream_subscriptions) == int
    assert type(aku_obj.total_stream_topics) == int


# Creates the object using the ENV variable and request the usage details to the API service
aku = APIKeyUser(request_info=True)
check_apikeyuser_types(aku)
assert aku.api_key == load_environment_value("FACTIVA_APIKEY")
assert aku.account_name != ''
assert aku.active_products != ''

# Creates an empty object from the ENV variablt with a value only for the api_key property
aku = APIKeyUser()
check_apikeyuser_types(aku)
assert aku.api_key == load_environment_value("FACTIVA_APIKEY")
assert aku.account_name == ''
assert aku.active_products == ''

# Creates an empty object from the provided string with a value only for the api_key property
aku = APIKeyUser('abcd1234abcd1234abcd1234abcd1234')
check_apikeyuser_types(aku)
assert aku.api_key == 'abcd1234abcd1234abcd1234abcd1234'
assert aku.account_name == ''
assert aku.active_products == ''

# TODO: Implement the test libraries to use assertEqual, assertNotEqual, assertRaises, etc.

# Creates an object from the provided string and request the usage details to the API service
# The key is invalid and this should validate how the error is processed
# aku = APIKeyUser('abcd1234abcd1234abcd1234abcd1234', request_info=True)

# Attempts to create an object with malformed keys
# aku = APIKeyUser('abc')
# aku = APIKeyUser('abcd1234abcd1234abcd1234abcd1234ab')
