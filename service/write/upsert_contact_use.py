from models.aton.nodes.data_dictionary.contact_use import ContactUse
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_contact_use import DD_ContactUse


def upsert_contact_use(contact_use: ContactUse, data_dictionary: DataDictionary):
    contact_use_node, is_created = ContactUse.get_or_create(contact_use)
    if is_created:
        data_dictionary.contact_use.connect(contact_use_node)
    for dd_contact_use in contact_use.context.get_dd_contact_use():
        dd_contact_use_node, is_dd_contact_use_created = DD_ContactUse.get_or_create(
            dd_contact_use
        )
        if dd_contact_use_node:
            contact_use_node.dd_contact_use.connect(dd_contact_use_node)
            dd_contact_use_node.context = dd_contact_use.context
            for legacy_id in dd_contact_use.context.get_legacy_ids():
                legacy_id.save()
                dd_contact_use_node.legacySystemIdentifier.connect(legacy_id)