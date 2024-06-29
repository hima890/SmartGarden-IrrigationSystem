from .resource import ESPResource
from .stat import Stat


class Report(ESPResource):

    def save(self):
        raise NotImplementedError('Report does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Report does not implement a destroy method')

    def stat(self):
        return Stat.for_report(self.id_)
