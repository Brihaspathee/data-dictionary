import weakref

from models.aton.nodes.data_dictionary.dd_healthcare_service_type import DD_HealthcareServiceType
from models.aton.nodes.data_dictionary.healthcare_service_types import HealthcareServiceTypes


class HealthcareServiceTypesContext:
    def __init__(self, healthcare_service_types: HealthcareServiceTypes):
        self.healthcare_service_types = weakref.proxy(healthcare_service_types)
        self.dd_healthcare_service_types: list[DD_HealthcareServiceType] = []

    def add_dd_healthcare_service_type(self, dd_healthcare_service_type: DD_HealthcareServiceType):
        self.dd_healthcare_service_types.append(dd_healthcare_service_type)

    def get_dd_healthcare_service_types(self):
        return self.dd_healthcare_service_types