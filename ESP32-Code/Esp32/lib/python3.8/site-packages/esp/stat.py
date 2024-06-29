from .resource import ESPResource
from .sdk import make_endpoint


class Stat(ESPResource):

    @classmethod
    def find(cls):
        raise NotImplementedError('Stat does not implement a find method')

    @classmethod
    def create(cls, **kwargs):
        raise NotImplementedError('Stat does not implement a create method')

    @classmethod
    def where(cls, **kwargs):
        raise NotImplementedError('Stat does not implement a where method')

    def save(self):
        raise NotImplementedError('Stat does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Stat does not implement a destroy method')

    @classmethod
    def for_report(cls, report_id):
        path = '/'.join(['reports', str(report_id), 'stats'])
        endpoint = make_endpoint(path)
        return cls._get(endpoint=endpoint)

    @classmethod
    def latest_for_teams(cls):
        path = '/'.join(['stats', 'latest_for_teams'])
        endpoint = make_endpoint(path)
        return cls._all(endpoint=endpoint)
