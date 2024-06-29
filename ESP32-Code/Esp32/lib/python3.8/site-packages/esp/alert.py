from .resource import ESPResource, make_endpoint
from .report import Report
from .suppression import (SuppressionRegion,
                          SuppressionSignature,
                          SuppressionUniqueIdentifier)


class Alert(ESPResource):

    @classmethod
    def create(cls):
        raise NotImplementedError('Alert does not implement a create method')

    def save(self):
        raise NotImplementedError('Alert does not implement a save method')

    def destroy(self):
        raise NotImplementedError('Alert does not implement a destroy method')

    @classmethod
    def where(cls, **clauses):
        if 'report_id' not in clauses:
            raise KeyError('report_id is required for filtering alerts')
        from_ = Report._resource_path(clauses['report_id'],
                                      extra=['alerts'])
        del clauses['report_id']
        clauses['from'] = from_
        return super(Alert, cls).where(**clauses)

    def suppress_region(self, reason):
        return self.suppress(SuppressionRegion, reason)

    def suppress_signature(self, reason):
        return self.suppress(SuppressionSignature, reason)

    def suppress_unique_identifier(self, reason):
        return self.suppress(SuppressionUniqueIdentifier, reason)

    def suppress(self, klass, reason):
        return klass.create(alert_id=self.id_, reason=reason)
