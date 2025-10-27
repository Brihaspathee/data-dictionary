from typing import Type, TypeVar

from neo4j.time import DateType
from neomodel import StringProperty, DateProperty, StructuredNode, RelationshipFrom
from neomodel.exceptions import DoesNotExist, MultipleNodesReturned


T = TypeVar("T", bound="Identifier")
class Identifier(StructuredNode):

    value: str= StringProperty(required=True)
    start_date: DateType= DateProperty(required=False, db_property='startDate')
    end_date: DateType= DateProperty(required=False, db_property='endDate')

    @classmethod
    def get_or_create(cls: Type[T], lookup_props: dict, other_props: dict) -> tuple[
        T, bool]:
        try:
            node = cls.nodes.get(**lookup_props)
            created = False
        except DoesNotExist:
            node = cls(**lookup_props, **other_props).save()
            created = True
        except MultipleNodesReturned as e:
            raise MultipleNodesReturned(
                f"Multiple nodes returned for {cls.__name__} with lookup props {lookup_props}"
            ) from e
        return node, created

class LegacySystemIdentifier(Identifier):
    _node_labels = ('Identifier', 'LegacySystemIdentifier')

    system: str= StringProperty(required=False)
    system_id_type: str= StringProperty(required=False, db_property='systemIdType')
    description: str= StringProperty(required=False)

    dd_specialty = RelationshipFrom('models.aton.nodes.data_dictionary.dd_specialty_type.DD_SpecialtyType', 'HAS_LEGACY_SYSTEM_IDENTIFIER')
    dd_qualification_type = RelationshipFrom('models.aton.nodes.data_dictionary.dd_qualification_type.DD_QualificationType',
                                    'HAS_LEGACY_SYSTEM_IDENTIFIER')
    dd_organization_type = RelationshipFrom('models.aton.nodes.data_dictionary.dd_organization_type.DD_OrganizationType',
                                    'HAS_LEGACY_SYSTEM_IDENTIFIER')
