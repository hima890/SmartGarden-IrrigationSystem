import unittest

import esp


class TestBase(unittest.TestCase):

    def setUp(self):
        esp.settings.settings.access_key_id = 'abc'
        esp.settings.settings.secret_access_key = 'abc123'
        esp.settings.settings.host = 'http://localhost:3000'
