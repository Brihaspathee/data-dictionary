from models.aton.nodes.data_dictionary.contact_use import ContactUse
from models.aton.nodes.data_dictionary.context.contact_use_context import ContactUseContext
from models.aton.nodes.data_dictionary.context.dd_contact_use_context import DDContactUseContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_contact_use import DD_ContactUse
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.contact_type import ContactTypesDC


def transform_contact_use(contact_types: ContactTypesDC, data_dictionary:DataDictionary):
    contact_use: ContactUse = ContactUse(definition="Contact Use node")
    contact_use.context = ContactUseContext(contact_use)
    for contact_type in contact_types.contactTypes:
        dd_contact_use: DD_ContactUse = DD_ContactUse(code=contact_type.code,
                                                        value=contact_type.value,
                                                        description=contact_type.description)
        dd_contact_use.context = DDContactUseContext(dd_contact_use)
        # contact_use.context.add_dd_contact_use(dd_contact_use)
        if contact_type.portico_contact_type and contact_type.systemIdType:
            legacy_id = LegacySystemIdentifier(value=contact_type.portico_contact_type,
                                               description=None,
                                               system=contact_type.system,
                                               system_id_type=contact_type.systemIdType)
            dd_contact_use.context.add_legacy_id(legacy_id)
        contact_use.context.add_dd_contact_use(dd_contact_use)
    data_dictionary.context.set_contact_use(contact_use)