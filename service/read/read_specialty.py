import os
import pandas as pd
from models.data_classes.specialtytype import Group, SpecialtyType, Classification, Specialization
import logging

log = logging.getLogger(__name__)

def read_specialty() -> SpecialtyType:
    log.debug("Reading specialty")
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    log.debug(f"Base dir {base_dir}")
    csv_path = os.path.join(base_dir, "dictionary_files", "specialty", "nucc_taxonomy_251.csv")

    df = pd.read_csv(csv_path)

    # If specialization column in the csv does not have a value, use the value in the classification column
    df['Specialization'] = df['Specialization'].fillna(df['Classification'])

    groups: list[Group] = []
    for group_name, group_df in df.groupby('Grouping'):
        classifications: list[Classification] = []
        for classification_name, classification_df in group_df.groupby('Classification'):
            specializations: list[Specialization] = []
            for _, row in classification_df.iterrows():
                specialization = Specialization(name=row['Specialization'],
                                                taxonomy=row['Code'],
                                                 definition=row['Definition'])
                specializations.append(specialization)
            classification = Classification(classificationName=classification_name,
                                            specializations=specializations)
            classifications.append(classification)
        group = Group(groupName=group_name,
                      classifications=classifications)
        groups.append(group)
    specialty:SpecialtyType = SpecialtyType(groups=groups)

    return specialty