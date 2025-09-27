from dataclasses import dataclass, field


@dataclass
class Specialization:
    name: str
    taxonomy: str
    definition: str

    def __str__(self):
        return (f"Specialization: {self.name},"
                f" taxonomy: {self.taxonomy},"
                f" definition: {self.definition}")

@dataclass
class Classification:
    classificationName: str
    specializations: list[Specialization] = field(default_factory=list)

    def __str__(self):
        return (f"SpecialtyClassification: {self.classificationName},"
                f" specializations: {self.specializations}")

@dataclass
class Group:
    groupName: str
    classifications: list[Classification] = field(default_factory=list)

    def __str__(self):
        return (f"SpecialtyGroup: {self.groupName},"
                f" specialtyClassifications: {self.classifications}")

@dataclass
class SpecialtyType:
    groups: list[Group] = field(default_factory=list)

    def __str__(self):
        return f"Specialty: {self.groups}"