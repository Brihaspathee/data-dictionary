import logging

from config import settings
from db import init_db
from models.data_classes.specialty_type import SpecialtyType
from service.read.read_specialty import read_specialty
from service.read.read_qualifications import read_qualifications
from service.transform.transform import transform
from service.write.upsert_data_dictionary import upsert_data_dictionary

log = logging.getLogger(__name__)

def main():
    log.debug("Starting...")
    log.debug(f"Running on {settings.ENVIRONMENT} environment")
    log.debug(f"NEO4J info {settings.NEO4J} environment")
    logging.basicConfig(level=logging.DEBUG)
    # read_qualifications()
    init_db()
    specialty: SpecialtyType = read_specialty()
    # log.debug(specialty)
    data_dictionary = transform(specialty, "specialty")
    upsert_data_dictionary(data_dictionary)
    log.debug("Finished!")


if __name__ == "__main__":
    main()