import unittest
from factiva.core import APIKeyUser
from factiva.helper import load_environment_value

FACTIVA_APIKEY = load_environment_value("FACTIVA_APIKEY")
DUMMY_KEY = 'abcd1234abcd1234abcd1234abcd1234'


class TestAPIKeyUser(unittest.TestCase):

    def test_create_user_with_env_key(self):
        aku = APIKeyUser(request_info=True)
        self.assertEqual(aku.api_key, FACTIVA_APIKEY)

    def test_create_user_with_key_dummy(self):
        aku = APIKeyUser(api_key=DUMMY_KEY)
        self.assertNotEqual(aku.api_key, FACTIVA_APIKEY)
    
    def test_create_user_with_invalid_key(self):
        with self.assertRaises(ValueError):
            APIKeyUser(api_key='aabbcc')
