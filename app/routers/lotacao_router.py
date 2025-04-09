from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.lotacao import Lotacao
from app.schemas.lotacao import LotacaoCreate, LotacaoUpdate, LotacaoOut
from app.auth.auth_handler import get_current_user

router = APIRouter(prefix="/lotacoes", tags=["Lotação"])

@router.post("/", response_model=LotacaoOut)
def create_lotacao(data: LotacaoCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    lotacao = Lotacao(**data.dict())
    db.add(lotacao)
    db.commit()
    db.refresh(lotacao)
    return lotacao

@router.get("/", response_model=List[LotacaoOut])
def list_lotacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(Lotacao).offset(skip).limit(limit).all()

@router.put("/{id}", response_model=LotacaoOut)
def update_lotacao(id: int, data: LotacaoUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    lotacao = db.query(Lotacao).filter(Lotacao.id == id).first()
    if not lotacao:
        raise HTTPException(status_code=404, detail="Lotação não encontrada")
    for key, value in data.dict().items():
        setattr(lotacao, key, value)
    db.commit()
    return lotacao

@router.delete("/{id}")
def delete_lotacao(id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    lotacao = db.query(Lotacao).filter(Lotacao.id == id).first()
    if not lotacao:
        raise HTTPException(status_code=404, detail="Lotação não encontrada")
    db.delete(lotacao)
    db.commit()
    return {"msg": "Lotação removida com sucesso"}
