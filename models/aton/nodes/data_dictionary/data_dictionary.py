from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo

from models.aton.nodes.data_dictionary.specialty_type import SpecialtyType


class DataDictionary(StructuredNode):
    definition: str = StringProperty(required=True)

    specialty = RelationshipTo('models.aton.nodes.data_dictionary.specialty_type.SpecialtyType', 'SPECIALTIES_DEFINED')
    qualification = RelationshipTo('models.aton.nodes.data_dictionary.qualification_types.QualificationTypes', 'QUALIFICATIONS_DEFINED')
    organization_types = RelationshipTo('models.aton.nodes.data_dictionary.organization_types.OrganizationTypes', 'ORGANIZATION_TYPES_DEFINED')
    contact_use = RelationshipTo('models.aton.nodes.data_dictionary.contact_use.ContactUse', 'CONTACT_USES_DEFINED')
    disorder_types = RelationshipTo('models.aton.nodes.data_dictionary.disorder_types.DisorderTypes', 'DISORDER_TYPES_DEFINED')
    healthcare_service_types = RelationshipTo('models.aton.nodes.data_dictionary.healthcare_service_types.HealthcareServiceTypes', 'HEALTHCARE_SERVICE_TYPES_DEFINED')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None
