from typing import Any
import logging

from models.aton.nodes.data_dictionary.context.dd_qualification_type_context import DDQualificationTypeContext
from models.aton.nodes.data_dictionary.context.qualification_types_context import QualificationTypesContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_qualification_type import DD_QualificationType
from models.aton.nodes.data_dictionary.qualification_types import QualificationTypes
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.qualification_type import QualTypes

log = logging.getLogger(__name__)


def transform_qualification(qual_types: QualTypes, data_dictionary:DataDictionary):
    qualification_types: QualificationTypes = QualificationTypes(definition="Qualification Types node")
    qualification_types.context = QualificationTypesContext(qualification_types)
    for qualification in qual_types.qualifications:
        dd_qual_type: DD_QualificationType = DD_QualificationType(code=qualification.code,
                                                                  value=qualification.value,
                                                                   description=qualification.description,
                                                                   classification=qualification.classification,
                                                                  issuer=qualification.issuer,
                                                                   acronym=qualification.acronym,
                                                                   applicable_entities=qualification.applicable_entities,
                                                                   reference_url=qualification.reference_url)
        dd_qual_type.context = DDQualificationTypeContext(dd_qual_type)
        if qualification.portico_ds and qualification.systemIdType:
            legacy_id = LegacySystemIdentifier(value=qualification.portico_ds,
                                               description=None,
                                               system=qualification.system,
                                               system_id_type=qualification.systemIdType)
            dd_qual_type.context.add_legacy_id(legacy_id)
        qualification_types.context.add_dd_qualification(dd_qual_type)
    data_dictionary.context.set_qualification_types(qualification_types)