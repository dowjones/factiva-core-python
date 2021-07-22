import unittest
from factiva.core import UserKey
from factiva.helper import load_environment_value

FACTIVA_USERKEY = load_environment_value("FACTIVA_USERKEY")
DUMMY_KEY = 'abcd1234abcd1234abcd1234abcd1234'


class TestUserKey(unittest.TestCase):

    def test_create_user_with_env_key(self):
        u = UserKey(stats=True)
        self.assertEqual(u.user_key, FACTIVA_USERKEY)

    def test_create_user_with_key_dummy(self):
        u = UserKey(user_key=DUMMY_KEY)
        self.assertNotEqual(u.user_key, FACTIVA_USERKEY)

    def test_create_user_with_invalid_key(self):
        with self.assertRaises(ValueError):
            UserKey(user_key='aabbcc')

    def test_fetch_cloud_token(self):
        u = UserKey()
        u.get_cloud_token()
        self.assertNotEqual(u.cloud_token, {})
