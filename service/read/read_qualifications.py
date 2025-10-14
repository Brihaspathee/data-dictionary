import os
import csv
import json
import logging
from typing import Dict, Any

from models.data_classes.qualification_type import Qualification, QualTypes

log = logging.getLogger(__name__)

def read_qualifications() -> QualTypes:
    log.info("Reading qualifications")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to qualification_types folder
    base_dir = os.path.join(project_root, "dictionary_files", "qualification_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Qualification types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    qual_data = {
        "qualification_data": [],
        "mapping_data": []
    }

    qualification_data = []
    portico_to_aton_mapping = []

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        log.error("Reading file: {}".format(filename))
        if filename.endswith("qualification_types.csv"):
            qualification_data = read_qual_csv(filename, base_dir)
        elif filename.endswith("portico_to_aton_mapping.csv"):
            portico_to_aton_mapping = read_qual_csv(filename, base_dir)

    # Convert to JSON string
    # json_output_qual = json.dumps(qualification_data, indent=2, ensure_ascii=False)
    # json_output_mapping = json.dumps(portico_to_aton_mapping, indent=2, ensure_ascii=False)
    # log.error("Qualification data written to: {}".format(json_output_qual))
    # log.error("Mapping data written to: {}".format(json_output_mapping))
    qual_data["qualification_data"] = qualification_data
    qual_data["mapping_data"] = portico_to_aton_mapping
    # map_qualification(qual_data)
    return map_qualification(qual_data)

def read_qual_csv(file_name:str, base_dir:str) -> list[dict[str, Any]]:
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
    return data

def map_qualification(qualifications_and_mapping:dict[str,list[dict[str, Any]]]) -> QualTypes:
    quals: list[Qualification] = []
    # The keys in the dictionary are "qualification_data" and "mapping_data"
    qualifications: list[dict[str, Any]] = qualifications_and_mapping["qualification_data"]
    for qualification in qualifications:
        log.debug(f"Qualification: {qualification}")
        aton_type:str = qualification["code"]
        applicable_entities: list[str] = []
        if qualification["applicableEntities"]:
            applicable_entities = qualification["applicableEntities"].split("|")
        mapping: dict[str, Any] = get_mapping_data(aton_type, qualifications_and_mapping["mapping_data"])
        if mapping:
            quals.append(Qualification(
                code=aton_type,
                value=qualification["value"],
                description=qualification["description"],
                classification=qualification["classification"],
                issuer=qualification["issuer"],
                acronym=qualification["acronym"],
                applicable_entities=applicable_entities,
                reference_url=qualification["referenceURL"],
                portico_ds=mapping["value"],
                system=mapping["system"],
                systemIdType=mapping["systemIdType"]
            ))
        else:
            quals.append(Qualification(
                code=aton_type,
                value=qualification["value"],
                description=qualification["description"],
                classification=qualification["classification"],
                issuer=qualification["issuer"],
                acronym=qualification["acronym"],
                applicable_entities=applicable_entities,
                reference_url=qualification["referenceURL"],
                portico_ds=None,
                system=None,
                systemIdType=None
            ))
    return QualTypes(qualifications=quals)

def get_mapping_data(aton_type: str, mapping_data:list[dict[str, Any]]) -> dict[str,Any] | None:
    for row in mapping_data:
        if row["aton_type"] == aton_type:
            return row
    return None