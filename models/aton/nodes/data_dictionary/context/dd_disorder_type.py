import weakref

from models.aton.nodes.data_dictionary.dd_disorder_type import DD_DisorderType
from models.aton.nodes.identifier import LegacySystemIdentifier


class DDDisorderTypeContext:
    def __init__(self, dd_disorder_type: DD_DisorderType):
        self.dd_disorder_type = weakref.proxy(dd_disorder_type)
        self.legacy_identifiers: list[LegacySystemIdentifier] = []

    def add_legacy_id(self, legacy_id: LegacySystemIdentifier):
        self.legacy_identifiers.append(legacy_id)

    def get_legacy_ids(self):
        return self.legacy_identifiers