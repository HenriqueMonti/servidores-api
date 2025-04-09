import os
import importlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
from app.database import Base, engine
Base.metadata.create_all(bind=engine)

ROUTERS_DIR = os.path.join(os.path.dirname(__file__), "routers")
for filename in os.listdir(ROUTERS_DIR):
    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = filename[:-3]
        import_path = f"app.routers.{module_name}"
        module = importlib.import_module(import_path)

        if hasattr(module, "router"):
            app.include_router(module.router)

# Liberar somente o domínio do backend (ajustar conforme hospedagem)
origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg": "API de Servidores Funcionando 🚀"}
