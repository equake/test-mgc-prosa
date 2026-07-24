from fastapi import FastAPI

from app.routes.cnpj import router as cnpj_router

app = FastAPI(title="API Validação CNPJ", version="1.0.0")

app.include_router(cnpj_router)
