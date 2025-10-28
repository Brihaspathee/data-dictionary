import weakref

from models.aton.nodes.data_dictionary.dd_disorder_type import DD_DisorderType
from models.aton.nodes.data_dictionary.disorder_types import DisorderTypes


class DisorderTypesContext:
    def __init__(self, disorder_types: DisorderTypes):
        self.disorder_types = weakref.proxy(disorder_types)
        self.dd_disorder_types: list[DD_DisorderType] = []

    def add_dd_disorder_type(self, dd_disorder_type: DD_DisorderType):
        self.dd_disorder_types.append(dd_disorder_type)

    def get_dd_disorder_types(self):
        return self.dd_disorder_types