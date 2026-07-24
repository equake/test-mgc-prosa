from fastapi import FastAPI

from app.routes.cnpj import router as cnpj_router
from app.routes.cpf import router as cpf_router

app = FastAPI(title="API Validação CNPJ e CPF", version="0.1.4")

app.include_router(cnpj_router)
app.include_router(cpf_router)
