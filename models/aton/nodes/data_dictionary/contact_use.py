from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, DoesNotExist


class ContactUse(StructuredNode):
    definition: str = StringProperty(required=True)

    dd_contact_use = RelationshipTo('models.aton.nodes.data_dictionary.dd_contact_use.DD_ContactUse',
                                          'DEFINED_BY')

    data_dictionary = RelationshipFrom('models.aton.nodes.data_dictionary.data_dictionary.DataDictionary',
                                       'CONTACT_USES_DEFINED')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "ContactUse") -> tuple["ContactUse", bool]:
        try:
            node = cls.nodes.get(definition=instance.definition)
            created = False
        except DoesNotExist:
            node = cls(definition=instance.definition).save()
            created = True

        node.context = instance.context
        return node, created