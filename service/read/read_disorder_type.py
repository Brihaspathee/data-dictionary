import os
from typing import Any

import logging

from models.data_classes.disorder_type import DisorderTypesDC, DisorderType
from service.read.read_util import read_csv

log = logging.getLogger(__name__)


def read_disorder_types() -> DisorderTypesDC:
    log.debug("Reading Disorder Types")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to disorder types folder
    base_dir = os.path.join(project_root, "dictionary_files", "disorder_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Disorder types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    do_data = {
        "disorder_data": [],
        "mapping_data": []
    }

    disorder_data = []
    portico_to_aton_mapping = []

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        log.debug("Reading file: {}".format(filename))
        if filename.endswith("disorder_types.csv"):
            disorder_data = read_csv(filename, base_dir)
        elif filename.endswith("portico_to_aton_mapping.csv"):
            portico_to_aton_mapping = read_csv(filename, base_dir)
    do_data["disorder_data"] = disorder_data
    do_data["mapping_data"] = portico_to_aton_mapping
    return map_disorder(do_data)

def map_disorder(disorders_and_mapping:dict[str,list[dict[str, Any]]]) -> DisorderTypesDC:
    disorders: list[DisorderType] = []
    dos: list[dict[str, Any]] = disorders_and_mapping["disorder_data"]
    for disorder in dos:
        log.debug(f"Disorder: {disorder}")
        aton_type:str = disorder["code"]
        mapping: dict[str, Any] = get_mapping_data(aton_type, disorders_and_mapping["mapping_data"])
        if mapping:
            disorders.append(DisorderType(
                code=aton_type,
                value=disorder["value"],
                description=disorder["description"],
                portico_disorder_type=mapping["value"],
                system=mapping["system"],
                systemIdType=mapping["systemIdType"]
            ))
        else:
            disorders.append(DisorderType(
                code=aton_type,
                value=disorder["value"],
                description=disorder["description"],
                portico_disorder_type=None,
                system=None,
                systemIdType=None
            ))
    return DisorderTypesDC(disorder_types=disorders)

def get_mapping_data(aton_type: str, mapping_data:list[dict[str, Any]]) -> dict[str,Any] | None:
    for row in mapping_data:
        if row["aton_type"] == aton_type:
            return row
    return None