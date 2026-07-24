from fastapi import APIRouter

from app.models.cpf import CpfRequest, CpfResponse
from app.services.cpf_service import validate_cpf, format_cpf

router = APIRouter(prefix="/cpf", tags=["CPF"])


@router.post("/validate", response_model=CpfResponse)
def validate_cpf_endpoint(request: CpfRequest):
    result = validate_cpf(request.cpf)
    formatted = format_cpf(request.cpf)
    return CpfResponse(valid=result["valid"], cpf=formatted, message=result["message"])
