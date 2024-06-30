import json
import mock
import unittest

import esp
from .base import TestBase


class TestReport(TestBase):

    def setUp(self):
        self.report = {
            'id': '1',
            'type': 'reports',
            'attributes': {
                'status': 'completed',
                'created_at': '2016-02-26T18:00:00.000Z',
                'updated_at': '2016-02-26T18:03:48.000Z',
            },
            'relationships': {
                'alerts': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/alerts.json'
                    }
                },
                'organization': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/organization.json'
                    }
                },
                'sub_organization': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/sub_organization.json'
                    }
                },
                'team': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/team.json'
                    }
                },
            }
        }

        self.queued_report = {
            'id': '1',
            'type': 'reports',
            'attributes': {
                'status': 'queued',
                'created_at': '2016-02-26T18:00:00.000Z',
                'updated_at': '2016-02-26T18:03:48.000Z',
            },
            'relationships': {
                'alerts': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/alerts.json'
                    }
                },
                'organization': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/organization.json'
                    }
                },
                'sub_organization': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/sub_organization.json'
                    }
                },
                'team': {
                    'links': {
                        'related': 'http://localhost:3000/api/v2/reports/1/team.json'
                    }
                },
            }
        }

        self.queued_report_response = json.dumps({'data': self.queued_report})
        self.report_response = json.dumps({'data': self.report})

        super(TestReport, self).setUp()

    @mock.patch('esp.sdk.requests.post')
    def test_can_create_reports(self, mock_post):
        mock_response = mock.Mock()
        mock_response.json.return_value = json.loads(
            self.queued_report_response)
        mock_post.return_value = mock_response

        report = esp.Report.create(team_id=4)

        self.assertIsInstance(report, esp.report.Report)
        self.assertEqual(report.status, 'queued')
        payload = json.dumps({'data': {'type':
                                       'reports',
                                       'attributes': {'team_id': 4}
                                       }
                              })
        self.assertEqual(mock_post.call_args[0],
                         ('http://localhost:3000/api/v2/reports',))
        self.assertEqual(mock_post.call_args[1]['data'],
                         payload)

    def test_report_cannot_be_saved(self):
        report = esp.Report(self.report)
        with self.assertRaises(NotImplementedError):
            report.save()

    def test_report_cannot_be_destroyed(self):
        report = esp.Report(self.report)
        with self.assertRaises(NotImplementedError):
            report.destroy()
