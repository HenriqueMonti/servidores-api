from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.servidor_temporario import ServidorTemporario
from app.schemas.servidor_temporario import ServidorTemporarioCreate, ServidorTemporarioUpdate, ServidorTemporarioOut
from app.auth.auth_handler import get_current_user

router = APIRouter(prefix="/temporarios", tags=["Servidor Temporario"])

@router.post("/", response_model=ServidorTemporarioOut)
def create_servidor(data: ServidorTemporarioCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    servidor = ServidorTemporario(**data.dict())
    db.add(servidor)
    db.commit()
    db.refresh(servidor)
    return servidor

@router.get("/", response_model=List[ServidorTemporarioOut])
def list_servidores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(ServidorTemporario).offset(skip).limit(limit).all()

@router.put("/{id}", response_model=ServidorTemporarioOut)
def update_servidor(id: int, data: ServidorTemporarioUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    servidor = db.query(ServidorTemporario).filter(ServidorTemporario.id == id).first()
    if not servidor:
        raise HTTPException(status_code=404, detail="Não encontrado")
    for key, value in data.dict().items():
        setattr(servidor, key, value)
    db.commit()
    return servidor

@router.delete("/{id}")
def delete_servidor(id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    servidor = db.query(ServidorTemporario).filter(ServidorTemporario.id == id).first()
    if not servidor:
        raise HTTPException(status_code=404, detail="Não encontrado")
    db.delete(servidor)
    db.commit()
    return {"msg": "Removido com sucesso"}
