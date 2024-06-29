from .resource import ESPResource


class Dashboard(ESPResource):

    @classmethod
    def find(cls, *args, **kwargs):
        raise NotImplementedError('Dashboard does not implement a find method')

    @classmethod
    def where(cls, *args, **kwargs):
        raise NotImplementedError('Dashboard does not implement a where method')

    def save(self):
        raise NotImplementedError('Dashboard does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Dashboard does not implement a destroy method')
