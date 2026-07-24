from fastapi import APIRouter

from app.models.cnpj import CnpjRequest, CnpjResponse
from app.services.cnpj_service import format_cnpj, validate_cnpj

router = APIRouter(prefix="/cnpj", tags=["CNPJ"])


@router.post("/validate", response_model=CnpjResponse)
def validate_cnpj_endpoint(request: CnpjRequest):
    result = validate_cnpj(request.cnpj)
    formatted = format_cnpj(request.cnpj)
    return CnpjResponse(valid=result["valid"], cnpj=formatted, message=result["message"])
