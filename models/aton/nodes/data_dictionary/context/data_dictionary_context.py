import weakref

from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.specialty import Specialty


class DataDictionaryContext:

    def __init__(self, data_dictionary:DataDictionary):
        self.data_dictionary = weakref.proxy(data_dictionary)
        self.specialty: Specialty | None = None

    def set_specialty(self, specialty):
        self.specialty = specialty

    def get_specialty(self):
        return self.specialty