import json
import mock

import esp
from .base import TestBase


class TestTeam(TestBase):

    def setUp(self):
        self.team = {
            'id': 1,
            'type': 'teams',
            'attributes': {
                'name': 'Default Team'
            },
            'relationships': {
                'external_accounts': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/external_accounts.json'
                    }
                },
                'organization': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/organizations/1.json'
                    }
                },
                'sub_organization': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/sub_organizations/1.json'
                    }
                }
            }
        }

        self.team_error = [{'meta': {'name': "can't be blank"},
                            'status': '422',
                            'title': "Name can't be blank"}]

        self.team_json = json.dumps({'data': self.team})
        new_team = self.team
        new_team['attributes']['name'] = 'New Noise'
        self.team_saved_json = json.dumps({'data': new_team})
        self.team_error_json = json.dumps({'errors': self.team_error})
        super(TestTeam, self).setUp()

    @mock.patch('esp.sdk.requests.get')
    @mock.patch('esp.sdk.requests.patch')
    def test_can_save_team(self, mock_patch, mock_get):
        mock_response_get = mock.Mock()
        mock_response_get.json.return_value = json.loads(self.team_json)
        mock_response_patch = mock.Mock()
        mock_response_patch.json.return_value = json.loads(self.team_saved_json)
        mock_get.return_value = mock_response_get
        mock_patch.return_value = mock_response_patch

        team = esp.Team.find(id=1)
        self.assertEqual(team.name, 'Default Team')
        team.name = 'New Noise'
        updated_team = team.save()

        self.assertTrue(mock_patch.called)
        self.assertEqual(updated_team.name, 'New Noise')

    @mock.patch('esp.sdk.requests.get')
    @mock.patch('esp.sdk.requests.patch')
    def test_errors_included_in_team_instance(self, mock_patch, mock_get):
        mock_response_get = mock.Mock()
        mock_response_get.json.return_value = json.loads(self.team_json)
        mock_response_patch = mock.Mock()
        mock_response_patch.json.return_value = json.loads(self.team_error_json)
        mock_response_patch.status_code = 422
        mock_get.return_value = mock_response_get
        mock_patch.return_value = mock_response_patch

        team = esp.Team.find(id=1)
        self.assertEqual(team.name, 'Default Team')
        team.name = ''
        updated_team = team.save()

        self.assertTrue(mock_patch.called)
        self.assertTrue(updated_team.errors)
        self.assertEquals(updated_team.errors[0], "Name can't be blank")
