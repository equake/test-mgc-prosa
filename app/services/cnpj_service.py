def validate_cnpj(cnpj: str) -> dict:
    if len(cnpj) != 14:
        return {"valid": False, "message": "CNPJ deve ter 14 dígitos"}

    if _is_all_same_digits(cnpj):
        return {"valid": False, "message": "CNPJ inválido: todos os dígitos são iguais"}

    dv1 = _calculate_digit(cnpj[:12], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    if dv1 != int(cnpj[12]):
        return {"valid": False, "message": "CNPJ inválido: primeiro dígito verificador incorreto"}

    dv2 = _calculate_digit(cnpj[:13], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    if dv2 != int(cnpj[13]):
        return {"valid": False, "message": "CNPJ inválido: segundo dígito verificador incorreto"}

    return {"valid": True, "message": "CNPJ válido"}


def format_cnpj(cnpj: str) -> str:
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"


def _is_all_same_digits(cnpj: str) -> bool:
    return len(set(cnpj)) == 1


def _calculate_digit(base: str, weights: list) -> int:
    total = sum(int(d) * w for d, w in zip(base, weights, strict=True))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder
