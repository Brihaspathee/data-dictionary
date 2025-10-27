import weakref

from models.aton.nodes.data_dictionary.dd_organization_type import DD_OrganizationType
from models.aton.nodes.data_dictionary.organization_types import OrganizationTypes


class OrganizationTypesContext:
    def __init__(self, organization_types: OrganizationTypes):
        self.organization_types = weakref.proxy(organization_types)
        self.dd_organization_types: list[DD_OrganizationType] = []

    def add_dd_organization_type(self, dd_organization_type: DD_OrganizationType):
        self.dd_organization_types.append(dd_organization_type)

    def get_dd_organization_types(self):
        return self.dd_organization_types