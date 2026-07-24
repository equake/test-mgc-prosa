import pytest

from app.services.cpf_service import (
    validate_cpf,
    format_cpf,
)


class TestValidateCpf:
    def test_cpf_valido(self):
        result = validate_cpf("12345678909")
        assert result["valid"] is True
        assert result["message"] == "CPF válido"

    def test_outro_cpf_valido(self):
        result = validate_cpf("52998224725")
        assert result["valid"] is True

    def test_primeiro_digito_incorreto(self):
        result = validate_cpf("12345678919")
        assert result["valid"] is False
        assert "primeiro dígito verificador" in result["message"]

    def test_segundo_digito_incorreto(self):
        result = validate_cpf("12345678900")
        assert result["valid"] is False
        assert "segundo dígito verificador" in result["message"]

    def test_segundo_digito_errado(self):
        result = validate_cpf("12345678901")
        assert result["valid"] is False
        assert "segundo dígito verificador" in result["message"]

    def test_todos_digitos_iguais(self):
        result = validate_cpf("11111111111")
        assert result["valid"] is False
        assert result["message"] == "CPF inválido: todos os dígitos são iguais"

    def test_zeros_repetidos(self):
        result = validate_cpf("00000000000")
        assert result["valid"] is False

    def test_tamanho_invalido_menor(self):
        result = validate_cpf("12345")
        assert result["valid"] is False
        assert "deve ter 11 dígitos" in result["message"]

    def test_tamanho_invalido_maior(self):
        result = validate_cpf("1234567890123")
        assert result["valid"] is False
        assert "deve ter 11 dígitos" in result["message"]

    def test_string_vazia(self):
        result = validate_cpf("")
        assert result["valid"] is False


class TestFormatCpf:
    def test_formato_padrao(self):
        result = format_cpf("12345678909")
        assert result == "123.456.789-09"

    def test_formato_outro_cpf(self):
        result = format_cpf("52998224725")
        assert result == "529.982.247-25"
