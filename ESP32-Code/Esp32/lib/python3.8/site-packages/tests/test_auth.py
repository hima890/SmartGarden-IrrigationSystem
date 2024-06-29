import mock
import unittest
from esp.auth import ESPAuth


class MockRequest(object):

    def __init__(self, url, body):
        self.url = url
        self.body = body
        self.headers = {}


class TestAuth(unittest.TestCase):

    def test_apiauth_can_sign_request(self):
        request = MockRequest('http://example.com/api/v2/external_accounts',
                              '{"data":{"attributes":{"name":"Testing"}}}')
        request.method = 'PATCH'
        ESPAuth._request_date = mock.MagicMock(
            return_value='Mon, 21 October 2015 04:20:01 GMT')
        auth = ESPAuth('abc', 'abc123')
        request = auth(request)

        self.assertEqual(request.headers['Authorization'],
                         'APIAuth abc:rJKRqR9sESjbIJgaYSQ23TPtlgA=')
