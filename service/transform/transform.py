from typing import Any

from models.aton.nodes.data_dictionary.context.data_dictionary_context import DataDictionaryContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.data_classes.organization_type import OrganizationTypesDC
from models.data_classes.qualification_type import QualTypes
from models.data_classes.specialty import Specialty
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
        else:
            return None
    return data_dictionary