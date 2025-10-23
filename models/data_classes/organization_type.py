from dataclasses import dataclass, field


@dataclass
class OrganizationCode:
    code: str
    value: str
    description: str
    portico_prov_type:str | None
    system: str | None
    systemIdType: str | None


    def __str__(self):
        return (f" code: {self.code},"
                f" value: {self.value}"
                f" description: {self.description},")

@dataclass
class OrganizationTypesDC:
    organizationCodes: list[OrganizationCode] = field(default_factory=list)

    def __str__(self):
        return f"OrganizationTypesDC: {self.organizationCodes}"