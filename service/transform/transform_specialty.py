from models.aton.nodes.data_dictionary.context.dd_specialty_context import DDSpecialtyContext
from models.aton.nodes.data_dictionary.context.specialty_context import SpecialtyContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_specialty_type import DD_SpecialtyType
from models.aton.nodes.data_dictionary.specialty_type import SpecialtyType
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.specialty import Specialty


def transform_specialty(specialty_type: Specialty, data_dictionary:DataDictionary):
    specialty: SpecialtyType = SpecialtyType(definition="Specialty node definition")
    specialty.context = SpecialtyContext(specialty)
    for specialization in specialty_type.specializations:
        dd_specialty = DD_SpecialtyType(code=specialization.code,
                                        value=specialization.value,
                                        description=specialization.description,
                                        group=specialization.group,
                                        classification=specialization.classification)
        dd_specialty.context = DDSpecialtyContext(dd_specialty)
        if specialization.spec_id:
            legacy_id = LegacySystemIdentifier(value=specialization.spec_id,
                                               description=specialization.portico_ds,
                                               system="PORTICO",
                                               system_id_type="SPEC_ID")
            dd_specialty.context.add_legacy_id(legacy_id)
        specialty.context.add_dd_specialty(dd_specialty)
    data_dictionary.context.set_specialty(specialty)

