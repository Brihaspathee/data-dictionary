import logging
from typing import Any

from db.portico_db import PorticoDB
from models.data_classes.contact_type import ContactTypesDC
from models.data_classes.disorder_type import DisorderTypesDC
from models.data_classes.healthcare_service_type import HealthcareServiceTypesDC
from models.data_classes.organization_type import OrganizationTypesDC
from models.data_classes.qualification_type import QualTypes
from models.data_classes.specialty import Specialty
from service.read.read_contact_type import read_contact_types
from service.read.read_disorder_type import read_disorder_types
from service.read.read_healthcare_service_type import read_healthcare_service_types
from service.read.read_organization_type import read_organization_types
from service.read.read_qualifications import read_qualifications
from service.read.read_spec_tax import read_spec_tax
from service.read.read_specialty import read_specialty

import logging

log = logging.getLogger(__name__)


def read_data_dictionary() -> list[Any]:
    data_dictionaries = []
    org_types: OrganizationTypesDC = read_organization_types()
    qual_types: QualTypes = read_qualifications()
    contact_types: ContactTypesDC = read_contact_types()
    disorder_types: DisorderTypesDC = read_disorder_types()
    healthcare_service_types: HealthcareServiceTypesDC = read_healthcare_service_types()
    log.debug(f"Disorder Types:{disorder_types}")
    log.debug(f"Healthcare Service Types:{healthcare_service_types}")
    portico_db: PorticoDB = PorticoDB()
    portico_db.connect()
    with portico_db.SessionLocal() as session:
        read_spec_tax(session)
    specialty: Specialty = read_specialty()
    data_dictionaries.append(qual_types)
    data_dictionaries.append(org_types)
    data_dictionaries.append(contact_types)
    data_dictionaries.append(specialty)
    data_dictionaries.append(disorder_types)
    data_dictionaries.append(healthcare_service_types)
    return data_dictionaries