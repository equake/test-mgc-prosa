import pytest

from app.services.cnpj_service import (
    validate_cnpj,
    format_cnpj,
    _is_all_same_digits,
    _calculate_digit,
)


class TestValidateCnpj:
    def test_cnpj_valido(self):
        result = validate_cnpj("11222333000181")
        assert result["valid"] is True
        assert result["message"] == "CNPJ válido"

    def test_outro_cnpj_valido(self):
        result = validate_cnpj("00000000000191")
        assert result["valid"] is True

    def test_primeiro_digito_incorreto(self):
        result = validate_cnpj("11222333000100")
        assert result["valid"] is False
        assert "primeiro dígito verificador" in result["message"]

    def test_segundo_digito_incorreto(self):
        result = validate_cnpj("11222333000180")
        assert result["valid"] is False
        assert "segundo dígito verificador" in result["message"]

    def test_todos_digitos_iguais(self):
        result = validate_cnpj("11111111111111")
        assert result["valid"] is False
        assert result["message"] == "CNPJ inválido: todos os dígitos são iguais"

    def test_zeros_repetidos(self):
        result = validate_cnpj("00000000000000")
        assert result["valid"] is False

    def test_tamanho_invalido_menor(self):
        result = validate_cnpj("12345")
        assert result["valid"] is False
        assert "deve ter 14 dígitos" in result["message"]

    def test_tamanho_invalido_maior(self):
        result = validate_cnpj("1234567890123456")
        assert result["valid"] is False
        assert "deve ter 14 dígitos" in result["message"]

    def test_string_vazia(self):
        result = validate_cnpj("")
        assert result["valid"] is False


class TestFormatCnpj:
    def test_formato_padrao(self):
        result = format_cnpj("11222333000181")
        assert result == "11.222.333/0001-81"

    def test_formato_zeros(self):
        result = format_cnpj("00000000000191")
        assert result == "00.000.000/0001-91"


class TestIsAllSameDigits:
    def test_all_same(self):
        assert _is_all_same_digits("11111111111111") is True

    def test_all_zeros(self):
        assert _is_all_same_digits("00000000000000") is True

    def test_diferentes(self):
        assert _is_all_same_digits("11222333000181") is False


class TestCalculateDigit:
    def test_base_conhecida(self):
        weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digit = _calculate_digit("112223330001", weights)
        assert digit == 8

    def test_restituio_zero(self):
        weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digit = _calculate_digit("1122233300018", weights)
        assert digit == 1
