import json
import mock

from .base import TestBase
from esp import ExternalAccount


class TestExternalAccount(TestBase):

    def setUp(self, *args, **kwargs):
        self.external_account = {
            'id': 1,
            'type': 'external_accounts',
            'attributes': {

            }
        }
        self.external_account_json = json.dumps({'data': self.external_account})

    @mock.patch('esp.sdk.requests.post')
    def test_external_account_create_generates_uuid(self, mock_post):
        mock_response = mock.Mock()
        mock_response.json.return_value = json.loads(self.external_account_json)
        mock_post.return_value = mock_response

        ExternalAccount.create(name='test',
                               arn='test',
                               external_id='11111111-1111-1111-1111-1111111111111',
                               team_id=1)

        self.assertIn('external_id', mock_post.call_args[1]['data'])
