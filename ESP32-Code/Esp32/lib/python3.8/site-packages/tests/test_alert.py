import esp
from .base import TestBase


class TestAlert(TestBase):

    def setUp(self):
        self.alert = {
            'id': '5',
            'type': 'alerts',
            'attributes': {
                'created_at': '2015-12-08T22:21:47.837Z',
                'status': 'fail',
                'resource': 'resource-6',
                'updated_at': '2015-12-08T22:21:47.844Z',
                'started_at': '2015-12-08T22:20:47.833Z',
                'ended_at': None
            },
            'relationships': {
                'external_account': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/external_accounts/6.json'
                    }
                },
                'region': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/regions/6.json'
                    }
                },
                'signature': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/signatures/4.json'
                    }
                },
                'custom_signature': {
                    'links': {
                        'related': None
                    }
                },
                'suppression': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/suppressions/1.json'
                    }
                },
                'metadata': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/alerts/5/metadata.json'
                    }
                },
                'cloud_trail_events': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/alerts/5/cloud_trail_events.json'
                    }
                },
                'tags': {
                    'links': {
                        'related': 'https://api.evident.io/api/v2/alerts/5/tags.json'
                    }
                }
            }
        }
        super(TestAlert, self).setUp()

    def test_alerts_cannot_be_saved(self):
        alert = esp.Alert(self.alert)
        with self.assertRaises(NotImplementedError):
            alert.save()

    def test_alerts_cannot_be_created(self):
        alert = esp.Alert(self.alert)
        with self.assertRaises(NotImplementedError):
            alert.create()

    def test_alerts_cannot_be_destroyed(self):
        alert = esp.Alert(self.alert)
        with self.assertRaises(NotImplementedError):
            alert.destroy()
