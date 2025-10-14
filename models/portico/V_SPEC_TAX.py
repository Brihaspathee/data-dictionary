from sqlalchemy import Column, String, Integer

from models.portico.base import Base


class SpecTax(Base):
    __tablename__ = 'v_spec_tax'
    __table_args__ = {'schema': 'portown'}

    spec_id = Column(Integer, primary_key=True)
    spec_ds = Column(String, nullable=False)
    taxonomy = Column(String, nullable=False)