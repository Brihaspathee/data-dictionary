import weakref

from models.aton.nodes.data_dictionary.dd_qualification_type import DD_QualificationType
from models.aton.nodes.data_dictionary.qualification_types import QualificationTypes


class QualificationTypesContext:

    def __init__(self, qualification_types: QualificationTypes):
        self.qualification_types = weakref.proxy(qualification_types)
        self.dd_qualifications: list[DD_QualificationType] = []

    def add_dd_qualification(self, dd_qualification: DD_QualificationType):
        self.dd_qualifications.append(dd_qualification)

    def get_dd_qualifications(self):
        return self.dd_qualifications