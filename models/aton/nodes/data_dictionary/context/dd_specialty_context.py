import weakref

from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.identifier import LegacySystemIdentifier


class DDSpecialtyContext:

    def __init__(self, dd_specialty:DD_Specialty):
        self.dd_specialty = weakref.proxy(dd_specialty)
        self.legacy_identifiers: list[LegacySystemIdentifier] = []

    def add_legacy_id(self, legacy_id: LegacySystemIdentifier):
        self.legacy_identifiers.append(legacy_id)

    def get_legacy_ids(self):
        return self.legacy_identifiers