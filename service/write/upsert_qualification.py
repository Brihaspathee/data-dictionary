from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_qualification_type import DD_QualificationType
from models.aton.nodes.data_dictionary.dd_specialty import DD_Specialty
from models.aton.nodes.data_dictionary.qualification_types import QualificationTypes
import logging

log = logging.getLogger(__name__)

def upsert_qualification(qualification_types: QualificationTypes, data_dictionary: DataDictionary):
    qualification_types_node, is_created = QualificationTypes.get_or_create(qualification_types)
    if is_created:
        data_dictionary.qualification.connect(qualification_types_node)
    for dd_qualification in qualification_types.context.get_dd_qualifications():
        dd_qualification_type_node, is_dd_qualification_type_created = DD_QualificationType.get_or_create(
            dd_qualification
        )
        if is_dd_qualification_type_created:
            qualification_types_node.dd_qualification_type.connect(dd_qualification_type_node)
            dd_qualification_type_node.context = dd_qualification.context
            for legacy_id in dd_qualification.context.get_legacy_ids():
                legacy_id.save()
                dd_qualification_type_node.legacySystemIdentifier.connect(legacy_id)