from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, DoesNotExist


class HealthcareServiceTypes(StructuredNode):
    definition: str = StringProperty(required=True)

    dd_healthcare_service_type = RelationshipTo('models.aton.nodes.data_dictionary.dd_healthcare_service_type.DD_HealthcareServiceType',
                                          'DEFINED_BY')

    data_dictionary = RelationshipFrom('models.aton.nodes.data_dictionary.data_dictionary.DataDictionary', 'HEALTHCARE_SERVICE_TYPES_DEFINED')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "HealthcareServiceTypes") -> tuple["HealthcareServiceTypes", bool]:
        try:
            node = cls.nodes.get(definition=instance.definition)
            created = False
        except DoesNotExist:
            node = cls(definition=instance.definition).save()
            created = True

        node.context = instance.context
        return node, created