import unittest
from factiva.core import UserKey
from factiva.core.tools import load_environment_value

FACTIVA_USERKEY = load_environment_value("FACTIVA_USERKEY")
DUMMY_KEY = 'abcd1234abcd1234abcd1234abcd1234'


class TestUserKey(unittest.TestCase):

    def test_create_user_with_env_key(self):
        u = UserKey(stats=True)
        self.assertEqual(u.key, FACTIVA_USERKEY)

    def test_create_user_with_key_dummy(self):
        u = UserKey(key=DUMMY_KEY)
        self.assertNotEqual(u.key, FACTIVA_USERKEY)

    def test_create_user_with_invalid_key(self):
        with self.assertRaises(ValueError):
            UserKey(key='aabbcc')

    def test_fetch_cloud_token(self):
        u = UserKey()
        u.get_cloud_token()
        self.assertNotEqual(u.cloud_token, {})
