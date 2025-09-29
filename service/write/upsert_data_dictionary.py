from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from service.write.upsert_specialty import upsert_specialty


def upsert_data_dictionary(data_dictionary: DataDictionary):
    dd = DataDictionary.nodes.get_or_none()
    if not dd:
        dd = data_dictionary.save()
    if data_dictionary.get_specialty():
        upsert_specialty(data_dictionary.get_specialty(), dd)