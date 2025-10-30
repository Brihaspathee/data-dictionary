from typing import Any

from models.aton.nodes.data_dictionary.context.data_dictionary_context import DataDictionaryContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.data_classes.contact_type import ContactTypesDC
from models.data_classes.disorder_type import DisorderTypesDC
from models.data_classes.healthcare_service_type import HealthcareServiceTypesDC
from models.data_classes.organization_type import OrganizationTypesDC
from models.data_classes.qualification_type import QualTypes
from models.data_classes.specialty import Specialty
from service.transform.transform_contact_use import transform_contact_use
from service.transform.transform_disorder_type import transform_disorder_type
from service.transform.transform_healthcare_service_type import transform_hs_type
from service.transform.transform_org_type import transform_org_type
from service.transform.transform_specialty import transform_specialty
from service.transform.transform_qualification import transform_qualification
import logging

log = logging.getLogger(__name__)


def transform(data_dictionaries: list[Any]) -> DataDictionary | None:
    data_dictionary: DataDictionary = DataDictionary(definition="Top level Data Dictionary node")
    data_dictionary.context = DataDictionaryContext(data_dictionary)
    for dictionary in data_dictionaries:
        if isinstance(dictionary, Specialty):
            transform_specialty(dictionary, data_dictionary)
        elif isinstance(dictionary, QualTypes):
            transform_qualification(dictionary, data_dictionary)
        elif isinstance(dictionary, OrganizationTypesDC):
            log.debug("Transforming organization types")
            transform_org_type(dictionary, data_dictionary)
        elif isinstance(dictionary, ContactTypesDC):
            transform_contact_use(dictionary, data_dictionary)
        elif isinstance(dictionary, DisorderTypesDC):
            transform_disorder_type(dictionary, data_dictionary)
        elif isinstance(dictionary, HealthcareServiceTypesDC):
            transform_hs_type(dictionary, data_dictionary)
        else:
            return None
    return data_dictionary