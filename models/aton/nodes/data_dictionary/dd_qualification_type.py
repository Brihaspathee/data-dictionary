from neomodel import StructuredNode, StringProperty, ArrayProperty


class DD_QualificationType(StructuredNode):
    value = StringProperty(required=True)
    issuer = StringProperty(required=False)
    short_description = StringProperty(required=False, db_property='shortDescription')
    long_description = StringProperty(required=False, db_property='longDescription')
    acronym = StringProperty(required=False, db_property='acronym')
    applicable_entities = ArrayProperty(required=True, db_property='applicableEntities')
    reference_url = StringProperty(required=False, db_property='referenceUrl')