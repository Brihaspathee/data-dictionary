import os
from typing import Any

import logging

from models.data_classes.healthcare_service_type import HealthcareServiceTypesDC, HealthcareServiceType
from service.read.read_util import read_csv

log = logging.getLogger(__name__)


def read_healthcare_service_types() -> HealthcareServiceTypesDC:
    log.debug("Reading Healthcare Service Types")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to healthcare service types folder
    base_dir = os.path.join(project_root, "dictionary_files", "healthcare_service_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Healthcare Service types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    hs_data = {
        "healthcare_service_data": [],
        "mapping_data": []
    }

    healthcare_service_data = []
    portico_to_aton_mapping = []

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        log.debug("Reading file: {}".format(filename))
        if filename.endswith("healthcare_service_types.csv"):
            healthcare_service_data = read_csv(filename, base_dir)
        elif filename.endswith("portico_to_aton_mapping.csv"):
            portico_to_aton_mapping = read_csv(filename, base_dir)
    hs_data["healthcare_service_data"] = healthcare_service_data
    hs_data["mapping_data"] = portico_to_aton_mapping
    return map_healthcare_service(hs_data)

def map_healthcare_service(hs_and_mapping:dict[str,list[dict[str, Any]]]) -> HealthcareServiceTypesDC:
    healthcare_service_types: list[HealthcareServiceType] = []
    hs_types: list[dict[str, Any]] = hs_and_mapping["healthcare_service_data"]
    for healthcare_service in hs_types:
        log.debug(f"Healthcare Service: {healthcare_service}")
        aton_type:str = healthcare_service["code"]
        mapping: dict[str, Any] = get_mapping_data(aton_type, hs_and_mapping["mapping_data"])
        if mapping:
            healthcare_service_types.append(HealthcareServiceType(
                code=aton_type,
                value=healthcare_service["value"],
                description=healthcare_service["description"],
                classification=healthcare_service["classification"],
                portico_hs_type=mapping["value"],
                system=mapping["system"],
                systemIdType=mapping["systemIdType"]
            ))
        else:
            healthcare_service_types.append(HealthcareServiceType(
                code=aton_type,
                value=healthcare_service["value"],
                description=healthcare_service["description"],
                classification=healthcare_service["classification"],
                portico_hs_type=None,
                system=None,
                systemIdType=None
            ))
    return HealthcareServiceTypesDC(healthcare_service_types=healthcare_service_types)

def get_mapping_data(aton_type: str, mapping_data:list[dict[str, Any]]) -> dict[str,Any] | None:
    for row in mapping_data:
        if row["aton_type"] == aton_type:
            return row
    return None