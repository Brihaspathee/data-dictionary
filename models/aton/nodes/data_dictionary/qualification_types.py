from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo, DoesNotExist


class QualificationTypes(StructuredNode):
    definition: str = StringProperty(required=True)

    dd_qualification_type = RelationshipTo('models.aton.nodes.data_dictionary.dd_qualification_type.DD_QualificationType', 'DEFINED_BY')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "QualificationTypes") -> tuple["QualificationTypes", bool]:
        try:
            node = cls.nodes.get(definition=instance.definition)
            created = False
        except DoesNotExist:
            node = cls(definition=instance.definition).save()
            created = True

        node.context = instance.context
        return node, created