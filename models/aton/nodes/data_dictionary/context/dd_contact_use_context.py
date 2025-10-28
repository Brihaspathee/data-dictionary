import weakref

from models.aton.nodes.data_dictionary.dd_contact_use import DD_ContactUse
from models.aton.nodes.identifier import LegacySystemIdentifier


class DDContactUseContext:
    def __init__(self, dd_contact_use: DD_ContactUse):
        self.dd_contact_use = weakref.proxy(dd_contact_use)
        self.legacy_identifiers: list[LegacySystemIdentifier] = []

    def add_legacy_id(self, legacy_id: LegacySystemIdentifier):
        self.legacy_identifiers.append(legacy_id)

    def get_legacy_ids(self):
        return self.legacy_identifiers