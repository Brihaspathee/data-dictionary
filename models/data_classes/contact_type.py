from dataclasses import dataclass, field


@dataclass
class ContactType:
    code: str
    value: str
    description: str
    portico_contact_type:str | None
    system: str | None
    systemIdType: str | None


    def __str__(self):
        return (f" code: {self.code},"
                f" value: {self.value}"
                f" description: {self.description},")

@dataclass
class ContactTypesDC:
    contactTypes: list[ContactType] = field(default_factory=list)

    def __str__(self):
        return f"ContactTypesDC: {self.contactTypes}"