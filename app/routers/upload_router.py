from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import List
from app.services.minio_service import upload_image, generate_presigned_url
from app.auth.auth_handler import get_current_user

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/foto")
def upload_foto(files: List[UploadFile] = File(...), user: str = Depends(get_current_user)):
    links = []
    for file in files:
        filename = upload_image(file)
        url = generate_presigned_url(filename)
        if url:
            links.append(url)
    if not links:
        raise HTTPException(status_code=500, detail="Erro no upload")
    return {"urls": links}
