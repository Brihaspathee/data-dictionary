import weakref

from models.aton.nodes.data_dictionary.dd_healthcare_service_type import DD_HealthcareServiceType
from models.aton.nodes.identifier import LegacySystemIdentifier


class DDHealthcareServiceTypeContext:
    def __init__(self, dd_healthcare_service_type: DD_HealthcareServiceType):
        self.dd_healthcare_service_type = weakref.proxy(dd_healthcare_service_type)
        self.legacy_identifiers: list[LegacySystemIdentifier] = []

    def add_legacy_id(self, legacy_id: LegacySystemIdentifier):
        self.legacy_identifiers.append(legacy_id)

    def get_legacy_ids(self):
        return self.legacy_identifiers