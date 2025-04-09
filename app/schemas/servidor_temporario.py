from pydantic import BaseModel
from datetime import date

class ServidorTemporarioBase(BaseModel):
    nome: str
    nascimento: date
    contrato_fim: date

class ServidorTemporarioCreate(ServidorTemporarioBase): pass
class ServidorTemporarioUpdate(ServidorTemporarioBase): pass

class ServidorTemporarioOut(ServidorTemporarioBase):
    id: int
    class Config:
        orm_mode = True
