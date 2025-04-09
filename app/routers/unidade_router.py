from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.unidade import Unidade
from app.schemas.unidade import UnidadeCreate, UnidadeUpdate, UnidadeOut
from app.auth.auth_handler import get_current_user

router = APIRouter(prefix="/unidades", tags=["Unidade"])

@router.post("/", response_model=UnidadeOut)
def create_unidade(unidade: UnidadeCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_unidade = Unidade(**unidade.dict())
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

@router.get("/", response_model=List[UnidadeOut])
def list_unidades(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(Unidade).offset(skip).limit(limit).all()

@router.put("/{unidade_id}", response_model=UnidadeOut)
def update_unidade(unidade_id: int, unidade: UnidadeUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    if not db_unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")
    for key, value in unidade.dict().items():
        setattr(db_unidade, key, value)
    db.commit()
    return db_unidade

@router.delete("/{unidade_id}")
def delete_unidade(unidade_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    if not db_unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")
    db.delete(db_unidade)
    db.commit()
    return {"msg": "Unidade removida com sucesso"}
