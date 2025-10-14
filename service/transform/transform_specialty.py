from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.specialty import Specialty
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.specialty_type import SpecialtyType


def transform_specialty(specialty_type: SpecialtyType) -> DataDictionary:
    specialty: Specialty = Specialty(definition="Specialty node definition")
    for specialization in specialty_type.specializations:
        dd_specialty = DD_Specialty(code=specialization.code,
                                    value=specialization.value,
                                    description=specialization.description,
                                    group=specialization.group,
                                    classification=specialization.classification)
        if specialization.spec_id:
            legacy_id = LegacySystemIdentifier(value=specialization.spec_id,
                                               description=specialization.portico_ds,
                                               system="PORTICO",
                                               system_id="SPEC_ID")
            dd_specialty.add_legacy_id(legacy_id)
        specialty.add_specialization(dd_specialty)
    data_dictionary: DataDictionary = DataDictionary(definition="Top level Data Dictionary node")
    data_dictionary.set_specialty(specialty)
    return data_dictionary

