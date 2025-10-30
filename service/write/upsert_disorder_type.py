from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_disorder_type import DD_DisorderType
from models.aton.nodes.data_dictionary.disorder_types import DisorderTypes


def upsert_disorder_type(disorder_types: DisorderTypes, data_dictionary: DataDictionary):
    disorder_types_node, is_created = DisorderTypes.get_or_create(disorder_types)
    if is_created:
        data_dictionary.disorder_types.connect(disorder_types_node)
    for dd_disorder_type in disorder_types.context.get_dd_disorder_types():
        dd_disorder_type_node, is_dd_disorder_type_created = DD_DisorderType.get_or_create(
            dd_disorder_type
        )
        if dd_disorder_type_node:
            disorder_types_node.dd_disorder_type.connect(dd_disorder_type_node)
            dd_disorder_type_node.context = dd_disorder_type.context
            for legacy_id in dd_disorder_type.context.get_legacy_ids():
                legacy_id.save()
                dd_disorder_type_node.legacySystemIdentifier.connect(legacy_id)