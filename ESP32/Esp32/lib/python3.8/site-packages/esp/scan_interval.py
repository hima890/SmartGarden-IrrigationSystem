from .resource import ESPResource


class ScanInterval(ESPResource):

    @classmethod
    def find(cls, id):
        return super(ESPResource, cls).find(id=id)
