import weakref

from models.aton.nodes.data_dictionary.contact_use import ContactUse
from models.aton.nodes.data_dictionary.dd_contact_use import DD_ContactUse


class ContactUseContext:
    def __init__(self, contact_use: ContactUse):
        self.contact_use = weakref.proxy(contact_use)
        self.dd_contact_use: list[DD_ContactUse] = []

    def add_dd_contact_use(self, dd_contact_use: DD_ContactUse):
        self.dd_contact_use.append(dd_contact_use)

    def get_dd_contact_use(self):
        return self.dd_contact_use