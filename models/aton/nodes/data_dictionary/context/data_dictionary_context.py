import weakref

from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.qualification_types import QualificationTypes
from models.aton.nodes.data_dictionary.specialty import Specialty


class DataDictionaryContext:

    def __init__(self, data_dictionary:DataDictionary):
        self.data_dictionary = weakref.proxy(data_dictionary)
        self.specialty: Specialty | None = None
        self.qualificationTypes: QualificationTypes | None = None

    def set_specialty(self, specialty):
        self.specialty = specialty

    def get_specialty(self):
        return self.specialty

    def set_qualification_types(self, qualification_types):
        self.qualificationTypes = qualification_types

    def get_qualification_types(self):
        return self.qualificationTypes