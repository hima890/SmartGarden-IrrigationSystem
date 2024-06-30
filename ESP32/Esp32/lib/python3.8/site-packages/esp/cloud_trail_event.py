from .resource import ESPResource
from .sdk import make_endpoint


class CloudTrailEvent(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('CloudTrailEvent does not implement a create method')

    @classmethod
    def where(cls, *args, **kwargs):
        raise NotImplementedError('CloudTrailEvent does not implement a where method')

    @classmethod
    def find(cls, id):
        # override find because this class doesn't support listing without
        # an alert id
        return super(CloudTrailEvent, cls).find(id=id)

    def save(self):
        raise NotImplementedError('CloudTrailEvent does not implement a save method')

    def destroy(self):
        raise NotImplementedError('CloudTrailEvent does not implement a destroy method')

    @classmethod
    def for_alert(cls, alert_id):
        path = '/'.join(['alerts', str(alert_id), 'cloud_trail_events'])
        endpoint = make_endpoint(path)
        return cls._all(endpoint=endpoint)
