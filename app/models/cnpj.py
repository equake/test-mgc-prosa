import re

from pydantic import BaseModel, field_validator


class CnpjRequest(BaseModel):
    cnpj: str

    @field_validator("cnpj")
    @classmethod
    def normalize_cnpj(cls, v: str) -> str:
        cleaned = re.sub(r"\D", "", v)
        if len(cleaned) != 14:
            raise ValueError("CNPJ deve ter 14 dígitos numéricos")
        return cleaned


class CnpjResponse(BaseModel):
    valid: bool
    cnpj: str
    message: str
