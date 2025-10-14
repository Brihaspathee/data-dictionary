from dataclasses import dataclass, field


@dataclass
class Qualification:
    code: str
    value: str
    description: str
    classification: str
    issuer: str
    acronym: str
    applicable_entities: list[str]
    reference_url: str
    portico_ds: str | None
    system: str | None
    systemIdType: str | None


    def __str__(self):
        return (f" code: {self.code},"
                f" value: {self.value}"
                f" description: {self.description},"
                f" classification: {self.classification},"
                f" issuer: {self.issuer},"
                f" acronym: {self.acronym},"
                f" applicable_entities: {self.applicable_entities},"
                f" reference_url: {self.reference_url},"
                f" portico_ds: {self.portico_ds}")

@dataclass
class QualTypes:
    qualifications: list[Qualification] = field(default_factory=list)

    def __str__(self):
        return f"Qualification: {self.qualifications}"