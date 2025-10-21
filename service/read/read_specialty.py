import os
import pandas as pd
from models.data_classes.specialty import Specialty, Specialization
import service.read.read_spec_tax as read_spec_tax
import logging

log = logging.getLogger(__name__)

def read_specialty() -> Specialty:
    log.debug("Reading specialty")
    log.debug(f"V_SPEC_TAX:{read_spec_tax.SPEC_TAX}")
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    log.debug(f"Base dir {base_dir}")
    csv_path = os.path.join(base_dir, "dictionary_files", "specialty", "nucc_taxonomy_251.csv")

    df = pd.read_csv(csv_path)

    # Transformation
    # If a specialization column in the csv does not have a value, use the value in the classification column
    df["Specialization"] = df["Specialization"].fillna(df["Classification"])

    specializations: list[Specialization] = []
    for group_name, group_df in df.groupby('Grouping'):
        for classification_name, classification_df in group_df.groupby('Classification'):
            for _, row in classification_df.iterrows():
                code = row['Code']
                value =  row['Specialization']
                description = row['Definition']
                classification = row['Classification']
                group = row['Grouping']
                if value != classification:
                    portico_ds = classification+": "+value
                else:
                    portico_ds = value
                try:
                    spec_id = read_spec_tax.SPEC_TAX[code]["spec_id"]
                except KeyError:
                    log.error(f"Code {code} not found in SPEC_TAX")
                    spec_id = None
                specialization = Specialization(code=code,
                                                value=value,
                                                description=description,
                                                group=group,
                                                classification=classification,
                                                portico_ds=portico_ds,
                                                spec_id=spec_id)
                log.debug(f"Specialization: {specialization}")
                specializations.append(specialization)
    specialty:Specialty = Specialty(specializations=specializations)

    return specialty