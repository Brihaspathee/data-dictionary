import logging

from config import settings
from db import init_db
from db.portico_db import PorticoDB
from models.data_classes.qualification_type import Qualification, QualTypes
from models.data_classes.specialty_type import SpecialtyType
from service.read.read_specialty import read_specialty
from service.read.read_spec_tax import read_spec_tax
from service.read.read_qualifications import read_qualifications
from service.transform.transform import transform
from service.write.upsert_data_dictionary import upsert_data_dictionary

log = logging.getLogger(__name__)

def main():
    log.debug("Starting...")
    log.debug(f"Running on {settings.ENVIRONMENT} environment")
    log.debug(f"NEO4J info {settings.NEO4J} environment")
    logging.basicConfig(level=logging.DEBUG)
    data_dictionaries = []
    qual_types: QualTypes = read_qualifications()
    log.error(f"Qualifications length: {len(qual_types.qualifications)}")
    log.error(f"Qualifications: {qual_types.qualifications}")
    data_dictionaries.append(qual_types)
    portico_db: PorticoDB = PorticoDB()
    portico_db.connect()
    init_db()
    with portico_db.SessionLocal() as session:
        read_spec_tax(session)
    specialty: SpecialtyType = read_specialty()
    data_dictionaries.append(specialty)
    data_dictionary = transform(data_dictionaries)
    upsert_data_dictionary(data_dictionary)
    # log.debug("Finished!")


if __name__ == "__main__":
    main()