from .resource import ESPResource
from .sdk import make_endpoint


class Tag(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('Tag does not implement a create method')

    @classmethod
    def where(cls, **kwargs):
        raise NotImplementedError('Tag does not implement a where method')

    def save(self):
        raise NotImplementedError('Tag does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Tag does not implement a destroy method')

    @classmethod
    def for_alert(cls, alert_id):
        path = '/'.join(['alerts', str(alert_id), 'tags'])
        endpoint = make_endpoint(path)
        return cls._all(endpoint=endpoint)
