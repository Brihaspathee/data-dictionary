from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipFrom, RelationshipTo, DoesNotExist


class DD_OrganizationType(StructuredNode):
    code = StringProperty(required=True)
    value = StringProperty(required=True)
    description = StringProperty(required=False, db_property='description')

    organization_types = RelationshipFrom('models.aton.nodes.data_dictionary.organization_types.OrganizationTypes',
                                          'DEFINED_BY')
    legacySystemIdentifier = RelationshipTo('models.aton.nodes.identifier.LegacySystemIdentifier',
                                            'HAS_LEGACY_SYSTEM_IDENTIFIER')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "DD_OrganizationType") -> tuple["DD_OrganizationType", bool]:
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