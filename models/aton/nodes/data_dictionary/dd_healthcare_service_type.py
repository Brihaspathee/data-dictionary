from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipFrom, RelationshipTo, DoesNotExist


class DD_HealthcareServiceType(StructuredNode):
    code = StringProperty(required=True)
    value = StringProperty(required=True)
    classification = StringProperty(required=False, db_property='classification')
    description = StringProperty(required=False, db_property='description')

    healthcare_service_types = RelationshipFrom('models.aton.nodes.data_dictionary.healthcare_service_types.HealthcareServiceTypes',
                                          'DEFINED_BY')
    legacySystemIdentifier = RelationshipTo('models.aton.nodes.identifier.LegacySystemIdentifier',
                                            'HAS_LEGACY_SYSTEM_IDENTIFIER')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "DD_HealthcareServiceType") -> tuple["DD_HealthcareServiceType", bool]:
        try:
            node = cls.nodes.get(code=instance.code)
            created = False
        except DoesNotExist:
            node = cls(value=instance.value,
                       code=instance.code,
                       description=instance.description).save()
            created = True
        node.context = instance.context
        return node, created