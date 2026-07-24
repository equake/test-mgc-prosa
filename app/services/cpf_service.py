def validate_cpf(cpf: str) -> dict:
    if len(cpf) != 11:
        return {"valid": False, "message": "CPF deve ter 11 dígitos"}

    if _is_all_same_digits(cpf):
        return {"valid": False, "message": "CPF inválido: todos os dígitos são iguais"}

    dv1 = _calculate_digit(cpf[:9], list(range(10, 1, -1)))
    if dv1 != int(cpf[9]):
        return {"valid": False, "message": "CPF inválido: primeiro dígito verificador incorreto"}

    dv2 = _calculate_digit(cpf[:10], list(range(11, 1, -1)))
    if dv2 != int(cpf[10]):
        return {"valid": False, "message": "CPF inválido: segundo dígito verificador incorreto"}

    return {"valid": True, "message": "CPF válido"}


def format_cpf(cpf: str) -> str:
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def _is_all_same_digits(value: str) -> bool:
    return len(set(value)) == 1


def _calculate_digit(base: str, weights: list) -> int:
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder
