from models.aton.nodes.data_dictionary.context.dd_organization_type_context import DDOrganizationTypeContext
from models.aton.nodes.data_dictionary.context.organization_types_context import OrganizationTypesContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_organization_type import DD_OrganizationType
from models.aton.nodes.data_dictionary.organization_types import OrganizationTypes
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.organization_type import OrganizationTypesDC


def transform_org_type(org_types: OrganizationTypesDC, data_dictionary:DataDictionary):
    organization_types: OrganizationTypes = OrganizationTypes(definition="Organization Types node")
    organization_types.context = OrganizationTypesContext(organization_types)
    for org_type in org_types.organizationCodes:
        dd_organization_type: DD_OrganizationType = DD_OrganizationType(code=org_type.code,
                                                                        value=org_type.value,
                                                                        description=org_type.description)
        dd_organization_type.context = DDOrganizationTypeContext(dd_organization_type)
        # organization_types.context.add_dd_organization_type(dd_organization_type)
        if org_type.portico_prov_type and org_type.systemIdType:
            legacy_id = LegacySystemIdentifier(value=org_type.portico_prov_type,
                                               description=None,
                                               system=org_type.system,
                                               system_id_type=org_type.systemIdType)
            dd_organization_type.context.add_legacy_id(legacy_id)
        organization_types.context.add_dd_organization_type(dd_organization_type)
    data_dictionary.context.set_organization_types(organization_types)