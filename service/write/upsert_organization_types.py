from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_organization_type import DD_OrganizationType
from models.aton.nodes.data_dictionary.organization_types import OrganizationTypes


def upsert_organization_type(organization_types: OrganizationTypes, data_dictionary: DataDictionary):
    organization_types_node, is_created = OrganizationTypes.get_or_create(organization_types)
    if is_created:
        data_dictionary.organization_types.connect(organization_types_node)
    for dd_organization_type in organization_types.context.get_dd_organization_types():
        dd_organization_type_node, is_dd_organization_type_created = DD_OrganizationType.get_or_create(
            dd_organization_type
        )
        if dd_organization_type_node:
            organization_types_node.dd_organization_type.connect(dd_organization_type_node)
            dd_organization_type_node.context = dd_organization_type.context
            for legacy_id in dd_organization_type.context.get_legacy_ids():
                legacy_id.save()
                dd_organization_type_node.legacySystemIdentifier.connect(legacy_id)