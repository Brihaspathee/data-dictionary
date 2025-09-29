from typing import Any

from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from service.transform.transform_specialty import transform_specialty


def transform(data: Any, dictionary: str) -> DataDictionary | None:
    if dictionary == "specialty":
        return transform_specialty(data)
    else:
        return None