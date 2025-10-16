from typing import Any

from models.aton.nodes.data_dictionary.context.data_dictionary_context import DataDictionaryContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.data_classes.qualification_type import QualTypes
from models.data_classes.specialty_type import SpecialtyType
from service.transform.transform_specialty import transform_specialty
from service.transform.transform_qualification import transform_qualification


def transform(data_dictionaries: list[Any]) -> DataDictionary | None:
    data_dictionary: DataDictionary = DataDictionary(definition="Top level Data Dictionary node")
    data_dictionary.context = DataDictionaryContext(data_dictionary)
    for dictionary in data_dictionaries:
        if isinstance(dictionary, SpecialtyType):
            transform_specialty(dictionary, data_dictionary)
        elif isinstance(dictionary, QualTypes):
            transform_qualification(dictionary, data_dictionary)
        else:
            return None
    return data_dictionary