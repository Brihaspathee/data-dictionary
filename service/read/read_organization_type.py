import csv
import os
from typing import Any

from models.data_classes.organization_type import OrganizationTypesDC, OrganizationCode
import logging

log = logging.getLogger(__name__)


def read_organization_types() -> OrganizationTypesDC:
    log.info("Reading Organization Types")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to organization types folder
    base_dir = os.path.join(project_root, "dictionary_files", "organization_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Organization types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    org_data = {
        "organization_data": [],
        "mapping_data": []
    }

    organization_data = []
    portico_to_aton_mapping = []

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        log.error("Reading file: {}".format(filename))
        if filename.endswith("organization_types.csv"):
            organization_data = read_org_csv(filename, base_dir)
        elif filename.endswith("portico_to_aton_mapping.csv"):
            portico_to_aton_mapping = read_org_csv(filename, base_dir)
    org_data["organization_data"] = organization_data
    org_data["mapping_data"] = portico_to_aton_mapping
    return map_organization(org_data)

def read_org_csv(file_name:str, base_dir:str) -> list[dict[str, Any]]:
    data: list[dict[str, Any]] = []
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Normalize headers (strip whitespace)
        reader.fieldnames = [f.strip() for f in reader.fieldnames]

        rows = []
        for row in reader:
            # Strip whitespace from values
            clean_row = {k.strip(): (v.strip() if v else "") for k, v in row.items()}
            # Skip empty rows (where all values are blank)
            if any(clean_row.values()):
                rows.append(clean_row)
        data = rows
        log.info(f"Portico to ATOM mapping data:{data}")
    return data

def map_organization(organizations_and_mapping:dict[str,list[dict[str, Any]]]) -> OrganizationTypesDC:
    orgs: list[OrganizationCode] = []
    organizations: list[dict[str, Any]] = organizations_and_mapping["organization_data"]
    for organization in organizations:
        log.debug(f"Organization: {organization}")
        aton_type:str = organization["code"]
        applicable_entities: list[str] = []
        mapping: dict[str, Any] = get_mapping_data(aton_type, organizations_and_mapping["mapping_data"])
        if mapping:
            orgs.append(OrganizationCode(
                code=aton_type,
                value=organization["value"],
                description=organization["description"],
                portico_prov_type=mapping["value"],
                system=mapping["system"],
                systemIdType=mapping["systemIdType"]
            ))
        else:
            orgs.append(OrganizationCode(
                code=aton_type,
                value=organization["value"],
                description=organization["description"],
                portico_prov_type=None,
                system=None,
                systemIdType=None
            ))
    return OrganizationTypesDC(organizationCodes=orgs)

def get_mapping_data(aton_type: str, mapping_data:list[dict[str, Any]]) -> dict[str,Any] | None:
    for row in mapping_data:
        if row["aton_type"] == aton_type:
            return row
    return None