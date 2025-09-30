from neomodel import StructuredNode, StringProperty, RelationshipTo
from neomodel.exceptions import DoesNotExist

from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.specialty_group import SpecialtyGroup


class Specialty(StructuredNode):

    definition: str = StringProperty(required=True)

    specialization = RelationshipTo('DD_Specialty', 'DEFINED_BY')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pending_specializations: list[DD_Specialty] = []

    def add_specialization(self, group: DD_Specialty):
        self._pending_specializations.append(group)

    def get_specializations(self):
        return self._pending_specializations


    @classmethod
    def get_or_create(cls, instance: "Specialty") -> tuple["Specialty", bool]:
        try:
            node = cls.nodes.get(definition=instance.definition)
            created = False
        except DoesNotExist:
            node = cls(definition=instance.definition).save()
            created = True

        node._pending_specializations = instance.get_specializations()
        return node, created