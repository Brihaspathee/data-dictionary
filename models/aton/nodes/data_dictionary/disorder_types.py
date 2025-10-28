from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, DoesNotExist


class DisorderTypes(StructuredNode):
    definition: str = StringProperty(required=True)

    dd_disorder_type = RelationshipTo('models.aton.nodes.data_dictionary.dd_disorder_type.DD_DisorderType',
                                          'DEFINED_BY')

    data_dictionary = RelationshipFrom('models.aton.nodes.data_dictionary.data_dictionary.DataDictionary', 'DISORDER_TYPES_DEFINED')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "DisorderTypes") -> tuple["DisorderTypes", bool]:
        try:
            node = cls.nodes.get(definition=instance.definition)
            created = False
        except DoesNotExist:
            node = cls(definition=instance.definition).save()
            created = True

        node.context = instance.context
        return node, created