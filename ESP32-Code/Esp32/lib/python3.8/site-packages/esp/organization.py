from .resource import ESPResource


class Organization(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('Organization does not implement a create method')

    def destroy(self):
        raise NotImplementedError('Organization does not implement a destroy method')
