import logging

from config import settings
from db import init_db
from db.portico_db import PorticoDB
from models.data_classes.contact_type import ContactTypesDC
from models.data_classes.organization_type import OrganizationTypesDC
from models.data_classes.qualification_type import QualTypes
from models.data_classes.specialty import Specialty
from service.read.read_contact_type import read_contact_types
from service.read.read_data_dictionary import read_data_dictionary
from service.read.read_organization_type import read_organization_types
from service.read.read_qualifications import read_qualifications
from service.read.read_spec_tax import read_spec_tax
from service.read.read_specialty import read_specialty
from service.transform.transform import transform
from service.write.upsert_data_dictionary import upsert_data_dictionary

log = logging.getLogger(__name__)

def main():
    log.debug("Starting...")
    log.debug(f"Running on {settings.ENVIRONMENT} environment")
    log.debug(f"NEO4J info {settings.NEO4J} environment")
    logging.basicConfig(level=logging.DEBUG)
    init_db()
    data_dictionaries = read_data_dictionary()
    data_dictionary = transform(data_dictionaries)
    upsert_data_dictionary(data_dictionary)
    log.debug("Finished!")


if __name__ == "__main__":
    main()