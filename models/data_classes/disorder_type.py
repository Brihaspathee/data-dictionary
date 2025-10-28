from dataclasses import dataclass, field


@dataclass
class DisorderType:
    code: str
    value: str
    description: str
    portico_disorder_type:str | None
    system: str | None
    systemIdType: str | None


    def __str__(self):
        return (f" code: {self.code},"
                f" value: {self.value}"
                f" description: {self.description},")

@dataclass
class DisorderTypesDC:
    disorder_types: list[DisorderType] = field(default_factory=list)

    def __str__(self):
        return f"DisorderTypesDC: {self.disorder_types}"