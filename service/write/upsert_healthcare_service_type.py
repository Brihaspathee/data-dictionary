from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_healthcare_service_type import DD_HealthcareServiceType
from models.aton.nodes.data_dictionary.healthcare_service_types import HealthcareServiceTypes

import logging

log = logging.getLogger(__name__)


def upsert_hs_type(healthcare_service_types: HealthcareServiceTypes, data_dictionary: DataDictionary):
    healthcare_service_types_node, is_created = HealthcareServiceTypes.get_or_create(healthcare_service_types)
    if is_created:
        data_dictionary.healthcare_service_types.connect(healthcare_service_types_node)
    dd_hs_count: int = 2
    for dd_healthcare_service_type in healthcare_service_types.context.get_dd_healthcare_service_types():
        dd_healthcare_service_type_node, is_dd_healthcare_service_type_created = DD_HealthcareServiceType.get_or_create(
            dd_healthcare_service_type
        )
        log.info(f"Healthcare service node count: {dd_hs_count}")
        log.info(f"Healthcare service node created {dd_healthcare_service_type_node.code}")
        if dd_healthcare_service_type_node:
            healthcare_service_types_node.dd_healthcare_service_type.connect(dd_healthcare_service_type_node)
            dd_healthcare_service_type_node.context = dd_healthcare_service_type.context
            for legacy_id in dd_healthcare_service_type.context.get_legacy_ids():
                legacy_id.save()
                dd_healthcare_service_type_node.legacySystemIdentifier.connect(legacy_id)
        dd_hs_count = dd_hs_count + 1