import weakref

from models.aton.nodes.data_dictionary.dd_qualification_type import DD_QualificationType
from models.aton.nodes.identifier import LegacySystemIdentifier


class DDQualificationTypeContext:
    def __init__(self, dd_qualification_type: DD_QualificationType):
        self.dd_qualification_type = weakref.proxy(dd_qualification_type)
        self.legacy_identifiers: list[LegacySystemIdentifier] = []

    def add_legacy_id(self, legacy_id: LegacySystemIdentifier):
        self.legacy_identifiers.append(legacy_id)

    def get_legacy_ids(self):
        return self.legacy_identifiers