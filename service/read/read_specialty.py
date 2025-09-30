import os
import pandas as pd
from models.data_classes.specialty_type import SpecialtyType, Specialization
import logging

log = logging.getLogger(__name__)

def read_specialty() -> SpecialtyType:
    log.debug("Reading specialty")
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    log.debug(f"Base dir {base_dir}")
    csv_path = os.path.join(base_dir, "dictionary_files", "specialty", "nucc_taxonomy_251.csv")

    df = pd.read_csv(csv_path)

    # Transformation
    # If a specialization column in the csv does not have a value, use the value in the classification column
    df["Specialization"] = df["Specialization"].fillna(df["Classification"])

    # df["Specialization"] = df.apply(
    #     lambda row: (
    #         row["Classification"] if pd.isna(row["Specialization"]) or row["Specialization"] == ""
    #         else f'{row["Classification"]}: {row["Specialization"]}'
    #     ),
    #     axis=1
    # )

    specializations: list[Specialization] = []
    for group_name, group_df in df.groupby('Grouping'):
        for classification_name, classification_df in group_df.groupby('Classification'):
            for _, row in classification_df.iterrows():
                specialization =  row['Specialization']
                classification = row['Classification']
                group = row['Grouping']
                taxonomy = row['Code']
                definition = row['Definition']
                value = specialization
                if specialization != classification:
                    log.debug(f"Specialization {specialization} != Classification {classification}")
                    value = f'{classification}: {specialization}'
                specialization = Specialization(specialization=specialization,
                                                taxonomy=taxonomy,
                                                 definition=definition,
                                                group=group,
                                                classification=classification,
                                                value=value)
                specializations.append(specialization)
    specialty:SpecialtyType = SpecialtyType(specializations=specializations)

    return specialty