from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.servidor_efetivo import ServidorEfetivo
from app.schemas.servidor_efetivo import ServidorEfetivoCreate, ServidorEfetivoUpdate, ServidorEfetivoOut
from app.auth.auth_handler import get_current_user

router = APIRouter(prefix="/efetivos", tags=["Servidor Efetivo"])

@router.post("/", response_model=ServidorEfetivoOut)
def create_servidor(data: ServidorEfetivoCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    servidor = ServidorEfetivo(**data.dict())
    db.add(servidor)
    db.commit()
    db.refresh(servidor)
    return servidor

@router.get("/", response_model=List[ServidorEfetivoOut])
def list_servidores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(ServidorEfetivo).offset(skip).limit(limit).all()

@router.put("/{id}", response_model=ServidorEfetivoOut)
def update_servidor(id: int, data: ServidorEfetivoUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    servidor = db.query(ServidorEfetivo).filter(ServidorEfetivo.id == id).first()
    if not servidor:
        raise HTTPException(status_code=404, detail="Não encontrado")
    for key, value in data.dict().items():
        setattr(servidor, key, value)
    db.commit()
    return servidor

@router.delete("/{id}")
def delete_servidor(id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    servidor = db.query(ServidorEfetivo).filter(ServidorEfetivo.id == id).first()
    if not servidor:
        raise HTTPException(status_code=404, detail="Não encontrado")
    db.delete(servidor)
    db.commit()
    return {"msg": "Removido com sucesso"}
