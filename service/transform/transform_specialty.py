from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.specialty import Specialty
from models.aton.nodes.data_dictionary.specialty_classification import SpecialtyClassification
from models.aton.nodes.data_dictionary.specialty_group import SpecialtyGroup
from models.data_classes.specialty_type import SpecialtyType


def transform_specialty(specialty_type: SpecialtyType) -> DataDictionary:
    specialty: Specialty = Specialty(definition="Specialty node definition")
    for group in specialty_type.groups:
        specialty_group = SpecialtyGroup(name=group.groupName)
        for classification in group.classifications:
            specialty_classification = SpecialtyClassification(
                name=classification.classificationName)
            specialty_group.add_classification(specialty_classification)
            for specialization in classification.specializations:
                dd_specialty = DD_Specialty(name=specialization.name,
                                            taxonomy=specialization.taxonomy,
                                            definition=specialization.definition)
                specialty_classification.add_specialization(dd_specialty)
        specialty.add_group(specialty_group)
    data_dictionary: DataDictionary = DataDictionary(definition="Top level Data Dictionary node")
    data_dictionary.set_specialty(specialty)
    return data_dictionary

