from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class Lotacao(Base):
    __tablename__ = "lotacoes"

    id = Column(Integer, primary_key=True, index=True)
    servidor_id = Column(Integer, ForeignKey("servidores_efetivos.id"), nullable=False)
    unidade_id = Column(Integer, ForeignKey("unidades.id"), nullable=False)
