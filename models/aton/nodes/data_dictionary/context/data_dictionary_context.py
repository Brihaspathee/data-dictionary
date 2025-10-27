import weakref

from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.organization_types import OrganizationTypes
from models.aton.nodes.data_dictionary.qualification_types import QualificationTypes
from models.aton.nodes.data_dictionary.specialty_type import SpecialtyType


class DataDictionaryContext:

    def __init__(self, data_dictionary:DataDictionary):
        self.data_dictionary = weakref.proxy(data_dictionary)
        self.specialty: SpecialtyType | None = None
        self.qualificationTypes: QualificationTypes | None = None
        self.organization_types: OrganizationTypes | None = None

    def set_specialty(self, specialty):
        self.specialty = specialty

    def get_specialty(self):
        return self.specialty

    def set_qualification_types(self, qualification_types):
        self.qualificationTypes = qualification_types

    def get_qualification_types(self):
        return self.qualificationTypes

    def set_organization_types(self, organization_types):
        self.organization_types = organization_types

    def get_organization_types(self):
        return self.organization_types