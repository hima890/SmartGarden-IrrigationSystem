from .resource import ESPResource, PATCH_REQUEST, find_class_for_resource
from .sdk import make_endpoint


class Suppression(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('Suppression does not implement a create method')

    def save(self):
        raise NotImplementedError('Suppression does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Suppression does not implement a destroy method')

    def deactivate(self):
        endpoint = make_endpoint('/'.join([self._resource_path(),
                                           'deactivate']))
        response = self._make_request(endpoint, PATCH_REQUEST)
        data = response.json()
        cls = find_class_for_resource(self.singular_name)
        if response.status_code == 422:
            return cls(errors=data['errors'])
        return cls(data['data'])


class SuppressionRegion(ESPResource):

    resource_type = 'suppressions'

    @classmethod
    def find(cls, *args, **kwargs):
        raise NotImplementedError('Suppressions do not support find()')

    @classmethod
    def where(cls, *args, **kwargs):
        raise NotImplementedError('Suppressions do not support where()')

    @classmethod
    def create(self, **kwargs):
        path_array = ['suppressions']
        if 'alert_id' in kwargs:
            path_array.extend(['alert', kwargs['alert_id']])
        path_array.append('regions')
        path = '/'.join(path_array)
        return super(SuppressionSignature, self).create(with_path=path,
                                                        **kwargs)


class SuppressionSignature(ESPResource):

    resource_type = 'suppressions'

    @classmethod
    def find(cls, *args, **kwargs):
        raise NotImplementedError('Suppressions do not support find()')

    @classmethod
    def where(cls, *args, **kwargs):
        raise NotImplementedError('Suppressions do not support where()')

    def save(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    @classmethod
    def create(self, **kwargs):
        path_array = ['suppressions']
        if 'alert_id' in kwargs:
            path_array.extend(['alert', kwargs['alert_id']])
        path_array.append('signatures')
        path = '/'.join(path_array)
        return super(SuppressionSignature, self).create(with_path=path,
                                                        **kwargs)


class SuppressionUniqueIdentifier(ESPResource):

    resource_type = 'suppressions'

    @classmethod
    def find(cls, *args, **kwargs):
        raise NotImplementedError('Suppressions do not support find()')

    @classmethod
    def where(cls, *args, **kwargs):
        raise NotImplementedError('Suppressions do not support where()')

    @classmethod
    def create(self, **kwargs):
        path_array = ['suppressions']
        if 'alert_id' in kwargs:
            path_array.extend(['alert', kwargs['alert_id']])
        path_array.append('unique_identifiers')
        path = '/'.join(path_array)
        return super(SuppressionSignature, self).create(with_path=path,
                                                        **kwargs)
