from models.aton.nodes.data_dictionary.context.dd_disorder_type_context import DDDisorderTypeContext
from models.aton.nodes.data_dictionary.context.disorder_types_context import DisorderTypesContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_disorder_type import DD_DisorderType
from models.aton.nodes.data_dictionary.disorder_types import DisorderTypes
from models.aton.nodes.identifier import LegacySystemIdentifier
from models.data_classes.disorder_type import DisorderTypesDC


def transform_disorder_type(do_types: DisorderTypesDC, data_dictionary:DataDictionary):
    disorder_types: DisorderTypes = DisorderTypes(definition="Disorder Types node")
    disorder_types.context = DisorderTypesContext(disorder_types)
    for disorder_type in do_types.disorder_types:
        dd_disorder_type: DD_DisorderType = DD_DisorderType(code=disorder_type.code,
                                                                        value=disorder_type.value,
                                                                        description=disorder_type.description)
        dd_disorder_type.context = DDDisorderTypeContext(dd_disorder_type)
        # organization_types.context.add_dd_organization_type(dd_organization_type)
        if disorder_type.portico_disorder_type and disorder_type.systemIdType:
            legacy_id = LegacySystemIdentifier(value=disorder_type.portico_disorder_type,
                                               description=None,
                                               system=disorder_type.system,
                                               system_id_type=disorder_type.systemIdType)
            dd_disorder_type.context.add_legacy_id(legacy_id)
        disorder_types.context.add_dd_disorder_type(dd_disorder_type)
    data_dictionary.context.set_disorder_types(disorder_types)