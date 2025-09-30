from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.specialty import Specialty
from models.aton.nodes.data_dictionary.specialty_classification import SpecialtyClassification
from models.aton.nodes.data_dictionary.specialty_group import SpecialtyGroup
from models.data_classes.specialty_type import SpecialtyType


def transform_specialty(specialty_type: SpecialtyType) -> DataDictionary:
    specialty: Specialty = Specialty(definition="Specialty node definition")
    for specialization in specialty_type.specializations:
        dd_specialty = DD_Specialty(specialization=specialization.specialization,
                                    taxonomy=specialization.taxonomy,
                                    definition=specialization.definition,
                                    group=specialization.group,
                                    classification=specialization.classification,
                                    value=specialization.value)
        specialty.add_specialization(dd_specialty)
    data_dictionary: DataDictionary = DataDictionary(definition="Top level Data Dictionary node")
    data_dictionary.set_specialty(specialty)
    return data_dictionary

