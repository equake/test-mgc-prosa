import re

from pydantic import BaseModel, field_validator


class CpfRequest(BaseModel):
    cpf: str

    @field_validator("cpf")
    @classmethod
    def normalize_cpf(cls, v: str) -> str:
        cleaned = re.sub(r"\D", "", v)
        if len(cleaned) != 11:
            raise ValueError("CPF deve ter 11 dígitos numéricos")
        return cleaned


class CpfResponse(BaseModel):
    valid: bool
    cpf: str
    message: str
