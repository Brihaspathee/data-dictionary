from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo

from models.aton.nodes.data_dictionary.specialty import Specialty


class DataDictionary(StructuredNode):
    definition: str = StringProperty(required=True)

    specialty = RelationshipTo('models.aton.nodes.data_dictionary.specialty.Specialty', 'SPECIALTIES_DEFINED')
    qualification = RelationshipTo('models.aton.nodes.data_dictionary.qualification_types.QualificationTypes', 'QUALIFICATIONS_DEFINED')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None
