from dataclasses import dataclass, field


@dataclass
class Specialization:
    code: str
    value: str
    description: str
    group: str
    classification: str
    portico_ds: str
    spec_id: str


    def __str__(self):
        return (f" code: {self.code},"
                f" value: {self.value}"
                f" description: {self.description},"
                f" group: {self.group},"
                f" classification: {self.classification},"
                f" portico_ds: {self.portico_ds},"
                f" spec_id: {self.spec_id}")

@dataclass
class SpecialtyType:
    specializations: list[Specialization] = field(default_factory=list)

    def __str__(self):
        return f"Specialty: {self.specializations}"