from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class ServidorEfetivo(Base):
    __tablename__ = "servidores_efetivos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    fotografia = Column(String, nullable=True)
