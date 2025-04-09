from minio import Minio
from minio.error import S3Error
from datetime import timedelta
import uuid
from fastapi import UploadFile
import os

MINIO_ENDPOINT = "minio:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "fotos"

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Garante que o bucket existe
if not client.bucket_exists(BUCKET_NAME):
    client.make_bucket(BUCKET_NAME)

def upload_image(file: UploadFile) -> str:
    ext = os.path.splitext(file.filename)[-1]
    filename = f"{uuid.uuid4()}{ext}"

    client.put_object(
        BUCKET_NAME,
        filename,
        file.file,
        length=-1,
        part_size=10*1024*1024,
        content_type=file.content_type
    )
    return filename

def generate_presigned_url(filename: str) -> str:
    try:
        url = client.presigned_get_object(
            BUCKET_NAME,
            filename,
            expires=timedelta(minutes=5)
        )
        return url
    except S3Error:
        return None
