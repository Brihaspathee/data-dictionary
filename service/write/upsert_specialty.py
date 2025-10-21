from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_specialty_type import DD_SpecialtyType
from models.aton.nodes.data_dictionary.specialty_type import SpecialtyType
import logging

log = logging.getLogger(__name__)

def upsert_specialty(specialty: SpecialtyType, data_dictionary: DataDictionary):
    specialty_node, is_created = SpecialtyType.get_or_create(specialty)
    if is_created:
        # log.debug(f"Specialty node created with element id {specialty_node.element_id}")
        data_dictionary.specialty.connect(specialty_node)
    for dd_specialty in specialty.context.get_dd_specialties():
        dd_specialty_node, is_dd_specialty_created = DD_SpecialtyType.get_or_create(
            dd_specialty
        )
        if is_dd_specialty_created:
            # log.debug(f"Specialization {dd_specialty_node.value} created with element id {dd_specialty_node.element_id}")
            specialty_node.specialization.connect(dd_specialty_node)
            dd_specialty_node.context = dd_specialty.context
            for legacy_id in dd_specialty.context.get_legacy_ids():
                legacy_id.save()
                dd_specialty_node.legacySystemIdentifier.connect(legacy_id)