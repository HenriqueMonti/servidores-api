from pydantic import BaseModel

class UnidadeBase(BaseModel):
    nome: str
    endereco: str

class UnidadeCreate(UnidadeBase):
    pass

class UnidadeUpdate(UnidadeBase):
    pass

class UnidadeOut(UnidadeBase):
    id: int

    class Config:
        orm_mode = True
