import os
import csv
import json
import logging
from typing import Dict, Any

log = logging.getLogger(__name__)

def read_qualifications() -> dict[str, list[dict[str, Any]]]:
    log.info("Reading qualifications")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to qualification_types folder
    base_dir = os.path.join(project_root, "dictionary_files", "qualification_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Qualification types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    category_map = {
        "accreditation": "accreditation",
        "license": "license",
        "certification": "certification",
        "training": "training"
    }

    qualification_data = {}

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        if filename.endswith(".csv"):
            # Determine category based on filename prefix
            category = next(
                (v for k, v in category_map.items() if filename.startswith(k)),
                None
            )
            if not category:
                continue  # skip unrelated files
            file_path = os.path.join(base_dir, filename)

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
                qualification_data[category] = rows
    # Convert to JSON string
    json_output = json.dumps(qualification_data, indent=2, ensure_ascii=False)
    log.info("Qualification data written to: {}".format(json_output))
    return qualification_data