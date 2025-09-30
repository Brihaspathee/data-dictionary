from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.specialty import Specialty
from models.aton.nodes.data_dictionary.specialty_classification import SpecialtyClassification
from models.aton.nodes.data_dictionary.specialty_group import SpecialtyGroup
import logging

log = logging.getLogger(__name__)

def upsert_specialty(specialty: Specialty, data_dictionary: DataDictionary):
    specialty_node, is_created = Specialty.get_or_create(specialty)
    if is_created:
        # log.debug(f"Specialty node created with element id {specialty_node.element_id}")
        data_dictionary.specialty.connect(specialty_node)
    for dd_specialty in specialty_node.get_specializations():
        dd_specialty_node, is_dd_specialty_created = DD_Specialty.get_or_create(
            dd_specialty
        )
        if is_dd_specialty_created:
            # log.debug(f"Specialization {dd_specialty_node.value} created with element id {dd_specialty_node.element_id}")
            specialty_node.specialization.connect(dd_specialty_node)