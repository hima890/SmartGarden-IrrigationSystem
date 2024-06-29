from .resource import ESPResource


class ContactRequest(ESPResource):

    @classmethod
    def find(cls):
        raise NotImplementedError('ContactRequest does not implement a find method')

    @classmethod
    def where(cls, *args, **kwargs):
        raise NotImplementedError('ContactRequest does not implement a where method')

    def save(self):
        raise NotImplementedError('ContactRequest does not implement a save method')

    def destroy(self):
        raise NotImplementedError('ContactRequest does not implement a destroy method')
