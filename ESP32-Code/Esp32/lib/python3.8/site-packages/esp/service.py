from .resource import ESPResource


class Service(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('Service does not implement a create method')

    def save(self):
        raise NotImplementedError('Service does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Service does not implement a destroy method')

