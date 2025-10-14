from typing import Any

from neomodel import StructuredNode, StringProperty, ArrayProperty, RelationshipFrom, RelationshipTo, DoesNotExist


class DD_QualificationType(StructuredNode):
    code = StringProperty(required=True)
    value = StringProperty(required=True)
    description = StringProperty(required=False, db_property='description')
    classification = StringProperty(required=False, db_property='classification')
    issuer = StringProperty(required=False)
    acronym = StringProperty(required=False, db_property='acronym')
    applicable_entities = ArrayProperty(required=True, db_property='applicableEntities')
    reference_url = StringProperty(required=False, db_property='referenceUrl')

    qualification = RelationshipFrom('models.aton.nodes.data_dictionary.qualification_types.QualificationTypes', 'DEFINED_BY')
    legacySystemIdentifier = RelationshipTo('models.aton.nodes.identifier.LegacySystemIdentifier',
                                            'HAS_LEGACY_SYSTEM_IDENTIFIER')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "DD_QualificationType") -> tuple["DD_QualificationType", bool]:
        try:
            node = cls.nodes.get(code=instance.code)
            created = False
        except DoesNotExist:
            node = cls(value=instance.value,
                       code=instance.code,
                       description=instance.description,
                       classification=instance.classification,
                       issuer=instance.issuer,
                       acronym=instance.acronym,
                       applicable_entities=instance.applicable_entities,
                       reference_url=instance.reference_url).save()
            created = True
        node.context = instance.context
        return node, created