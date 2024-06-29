from .resource import ESPResource


class Region(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('Region does not implement a create method')

    def save(self):
        raise NotImplementedError('Region does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Region does not implement a destroy method')
