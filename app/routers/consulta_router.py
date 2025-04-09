from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from app.database import get_db
from app.models.servidor_efetivo import ServidorEfetivo
from app.models.unidade import Unidade
from app.models.lotacao import Lotacao
from app.auth.auth_handler import get_current_user

router = APIRouter(prefix="/consultas", tags=["Consultas"])

@router.get("/efetivos/unidade/{unid_id}")
def servidores_por_unidade(unid_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    results = (
        db.query(
            ServidorEfetivo.nome,
            func.date_part('year', func.age(ServidorEfetivo.nascimento)).label("idade"),
            Unidade.nome.label("unidade"),
            ServidorEfetivo.fotografia
        )
        .join(Lotacao, Lotacao.servidor_id == ServidorEfetivo.id)
        .join(Unidade, Unidade.id == Lotacao.unidade_id)
        .filter(Unidade.id == unid_id)
        .all()
    )
    return results

@router.get("/endereco")
def endereco_por_nome(nome: str, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    result = (
        db.query(Unidade.endereco)
        .join(Lotacao, Lotacao.unidade_id == Unidade.id)
        .join(ServidorEfetivo, ServidorEfetivo.id == Lotacao.servidor_id)
        .filter(ServidorEfetivo.nome.ilike(f"%{nome}%"))
        .distinct()
        .all()
    )
    if not result:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")
    return [r.endereco for r in result]
