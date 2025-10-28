from dataclasses import dataclass, field


@dataclass
class HealthcareServiceType:
    code: str
    value: str
    description: str
    classification: str
    portico_hs_type:str | None
    system: str | None
    systemIdType: str | None


    def __str__(self):
        return (f" code: {self.code},"
                f" value: {self.value}"
                f" description: {self.description},")

@dataclass
class HealthcareServiceTypesDC:
    healthcare_service_types: list[HealthcareServiceType] = field(default_factory=list)

    def __str__(self):
        return f"HealthcareServiceTypesDC: {self.healthcare_service_types}"