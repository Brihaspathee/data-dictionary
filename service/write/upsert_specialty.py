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
        log.debug("Specialty node created")
        data_dictionary.specialty.connect(specialty_node)
    for specialty_group in specialty_node.get_groups():
        specialty_group_node, is_group_created = SpecialtyGroup.get_or_create(
            specialty_group
        )
        if is_group_created:
            log.debug(f"Specialty group {specialty_group.name} created")
            specialty_node.groups.connect(specialty_group_node)
        for specialty_classification in specialty_group.get_classifications():
            specialty_classification_node, is_classification_created = SpecialtyClassification.get_or_create(
                specialty_classification
            )
            if is_classification_created:
                log.debug(f"Specialty classification {specialty_classification.name} created")
                specialty_group_node.classifications.connect(specialty_classification_node)
            for specialization in specialty_classification.get_specializations():
                specialization_node, is_specialization_created = DD_Specialty.get_or_create(
                    specialization
                )
                if is_specialization_created:
                    log.debug(f"Specialization {specialization.name} created")
                    specialty_classification_node.specialties.connect(specialization_node)