from models.aton.nodes.data_dictionary.context.dd_healthcare_service_type_context import DDHealthcareServiceTypeContext
from models.aton.nodes.data_dictionary.context.healthcare_service_type_context import HealthcareServiceTypesContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_healthcare_service_type import DD_HealthcareServiceType
from models.aton.nodes.data_dictionary.healthcare_service_types import HealthcareServiceTypes
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.healthcare_service_type import HealthcareServiceTypesDC


def transform_hs_type(hs_types: HealthcareServiceTypesDC, data_dictionary:DataDictionary):
    healthcare_service_types: HealthcareServiceTypes = HealthcareServiceTypes(definition="Healthcare Services Types node")
    healthcare_service_types.context = HealthcareServiceTypesContext(healthcare_service_types)
    for healthcare_service_type in hs_types.healthcare_service_types:
        dd_healthcare_service_type: DD_HealthcareServiceType = DD_HealthcareServiceType(code=healthcare_service_type.code,
                                                                        value=healthcare_service_type.value,
                                                                        classification=healthcare_service_type.classification,
                                                                        description=healthcare_service_type.description)
        dd_healthcare_service_type.context = DDHealthcareServiceTypeContext(dd_healthcare_service_type)
        if healthcare_service_type.portico_hs_type and healthcare_service_type.systemIdType:
            legacy_id = LegacySystemIdentifier(value=healthcare_service_type.portico_hs_type,
                                               description=None,
                                               system=healthcare_service_type.system,
                                               system_id_type=healthcare_service_type.systemIdType)
            dd_healthcare_service_type.context.add_legacy_id(legacy_id)
        healthcare_service_types.context.add_dd_healthcare_service_type(dd_healthcare_service_type)
    data_dictionary.context.set_healthcare_service_types(healthcare_service_types)