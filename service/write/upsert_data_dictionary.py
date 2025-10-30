from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from service.write.upsert_contact_use import upsert_contact_use
from service.write.upsert_disorder_type import upsert_disorder_type
from service.write.upsert_healthcare_service_type import upsert_hs_type
from service.write.upsert_organization_types import upsert_organization_type
from service.write.upsert_specialty import upsert_specialty
from service.write.upsert_qualification import upsert_qualification
import logging

log = logging.getLogger(__name__)


def upsert_data_dictionary(data_dictionary: DataDictionary):
    dd = DataDictionary.nodes.get_or_none()
    if not dd:
        dd = data_dictionary.save()
    if data_dictionary.context.get_specialty():
        upsert_specialty(data_dictionary.context.get_specialty(), dd)
    if data_dictionary.context.get_qualification_types():
        upsert_qualification(data_dictionary.context.get_qualification_types(), dd)
    if data_dictionary.context.get_organization_types():
        log.debug("Upserting organization types")
        upsert_organization_type(data_dictionary.context.get_organization_types(), dd)
    if data_dictionary.context.get_contact_use():
        log.info("Upserting contact use")
        upsert_contact_use(data_dictionary.context.get_contact_use(), dd)
    if data_dictionary.context.get_disorder_types():
        upsert_disorder_type(data_dictionary.context.get_disorder_types(), dd)
    if data_dictionary.context.get_healthcare_service_types():
        upsert_hs_type(data_dictionary.context.get_healthcare_service_types(), dd)