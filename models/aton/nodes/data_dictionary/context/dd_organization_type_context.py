import weakref

from models.aton.nodes.data_dictionary.dd_organization_type import DD_OrganizationType
from models.aton.nodes.identifier import LegacySystemIdentifier


class DDOrganizationTypeContext:
    def __init__(self, dd_organization_type: DD_OrganizationType):
        self.dd_organization_type = weakref.proxy(dd_organization_type)
        self.legacy_identifiers: list[LegacySystemIdentifier] = []

    def add_legacy_id(self, legacy_id: LegacySystemIdentifier):
        self.legacy_identifiers.append(legacy_id)

    def get_legacy_ids(self):
        return self.legacy_identifiers