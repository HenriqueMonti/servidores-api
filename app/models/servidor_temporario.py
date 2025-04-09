from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class ServidorTemporario(Base):
    __tablename__ = "servidores_temporarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    contrato_fim = Column(Date, nullable=False)
