import weakref

from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.specialty import Specialty
from models.data_classes.specialty_type import Specialization


class SpecialtyContext:

    def __init__(self, specialty:Specialty):
        self.specialization = weakref.proxy(specialty)
        self.dd_specialties: list[DD_Specialty] = []

    def add_dd_specialty(self, dd_specialty:DD_Specialty):
        self.dd_specialties.append(dd_specialty)

    def get_dd_specialties(self):
        return self.dd_specialties