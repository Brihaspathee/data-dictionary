import csv
import os
from typing import Any


def read_csv(file_name:str, base_dir:str) -> list[dict[str, Any]]:
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