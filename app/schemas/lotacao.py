from pydantic import BaseModel

class LotacaoBase(BaseModel):
    servidor_id: int
    unidade_id: int

class LotacaoCreate(LotacaoBase): pass
class LotacaoUpdate(LotacaoBase): pass

class LotacaoOut(LotacaoBase):
    id: int
    class Config:
        orm_mode = True
