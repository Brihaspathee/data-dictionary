import weakref

from models.aton.nodes.data_dictionary.dd_specialty_type import DD_SpecialtyType
from models.aton.nodes.data_dictionary.specialty_type import SpecialtyType
from models.data_classes.specialty import Specialization


class SpecialtyContext:

    def __init__(self, specialty:SpecialtyType):
        self.specialization = weakref.proxy(specialty)
        self.dd_specialties: list[DD_SpecialtyType] = []

    def add_dd_specialty(self, dd_specialty:DD_SpecialtyType):
        self.dd_specialties.append(dd_specialty)

    def get_dd_specialties(self):
        return self.dd_specialties