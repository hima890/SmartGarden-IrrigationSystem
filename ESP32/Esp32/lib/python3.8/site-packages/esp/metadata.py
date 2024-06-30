from .resource import ESPResource


class Metadata(ESPResource):

    @classmethod
    def for_alert(cls, alert_id):
        pass

    @classmethod
    def find(cls, id):
        """
        Overriding ESPResource's find because this resource does not support
        listing. This ensures an error is raised if no id is passed as a param

        :param id: ID of the metadata resource you are trying to fetch
        :type id: int
        :returns: Metadata instance
        """
        return super(Metadata, cls).find(id=id)

    @classmethod
    def create(cls):
        raise NotImplementedError('Metadata does not implement a create method')

    def save(self):
        raise NotImplementedError('Metadata does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Metadata does not implement a destroy method')
