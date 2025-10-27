import csv
import os
from typing import Any

from models.data_classes.contact_type import ContactTypesDC, ContactType
import logging

from service.read.read_util import read_csv

log = logging.getLogger(__name__)


def read_contact_types() -> ContactTypesDC:
    log.info("Reading Contact Types")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to organization types folder
    base_dir = os.path.join(project_root, "dictionary_files", "contact_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Contact types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    cntct_data = {
        "contact_data": [],
        "mapping_data": []
    }

    contact_data = []
    portico_to_aton_mapping = []

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        log.debug("Reading file: {}".format(filename))
        if filename.endswith("contact_use.csv"):
            contact_data = read_csv(filename, base_dir)
        elif filename.endswith("portico_to_aton_mapping.csv"):
            portico_to_aton_mapping = read_csv(filename, base_dir)
    cntct_data["contact_data"] = contact_data
    cntct_data["mapping_data"] = portico_to_aton_mapping
    return map_contact(cntct_data)

def map_contact(contacts_and_mapping:dict[str,list[dict[str, Any]]]) -> ContactTypesDC:
    contact_type_list: list[ContactType] = []
    contacts: list[dict[str, Any]] = contacts_and_mapping["contact_data"]
    for contact in contacts:
        log.info(f"Contact: {contact}")
        aton_type:str = contact["code"]
        mapping: dict[str, Any] = get_mapping_data(aton_type, contacts_and_mapping["mapping_data"])
        if mapping:
            contact_type_list.append(ContactType(
                code=aton_type,
                value=contact["value"],
                description=contact["description"],
                portico_contact_type=contact["value"],
                system=mapping["system"],
                systemIdType=mapping["systemIdType"]
            ))
        else:
            contact_type_list.append(ContactType(
                code=aton_type,
                value=contact["value"],
                description=contact["description"],
                portico_contact_type=None,
                system=None,
                systemIdType=None
            ))
    return ContactTypesDC(contactTypes=contact_type_list)

def get_mapping_data(aton_type: str, mapping_data:list[dict[str, Any]]) -> dict[str,Any] | None:
    for row in mapping_data:
        if row["aton_type"] == aton_type:
            return row
    return None