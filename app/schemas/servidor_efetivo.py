from pydantic import BaseModel
from datetime import date

class ServidorEfetivoBase(BaseModel):
    nome: str
    nascimento: date
    fotografia: str | None = None

class ServidorEfetivoCreate(ServidorEfetivoBase):
    pass

class ServidorEfetivoUpdate(ServidorEfetivoBase):
    pass

class ServidorEfetivoOut(ServidorEfetivoBase):
    id: int

    class Config:
        orm_mode = True
