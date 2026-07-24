import pytest
from pydantic import ValidationError

from app.models.cpf import CpfRequest, CpfResponse


class TestCpfRequest:
    def test_cpf_puro_funciona(self):
        data = CpfRequest(cpf="12345678909")
        assert data.cpf == "12345678909"

    def test_cpf_com_mascara_e_normalizado(self):
        data = CpfRequest(cpf="123.456.789-09")
        assert data.cpf == "12345678909"

    def test_mascara_alternativa(self):
        data = CpfRequest(cpf="123 456 789 09")
        assert data.cpf == "12345678909"

    def test_menos_de_11_digitos_lanca_erro(self):
        with pytest.raises(ValidationError):
            CpfRequest(cpf="12345")

    def test_mais_de_11_digitos_lanca_erro(self):
        with pytest.raises(ValidationError):
            CpfRequest(cpf="1234567890123")

    def test_string_vazia_lanca_erro(self):
        with pytest.raises(ValidationError):
            CpfRequest(cpf="")

    def test_apenas_pontuacao_lanca_erro(self):
        with pytest.raises(ValidationError):
            CpfRequest(cpf="...---")


class TestCpfResponse:
    def test_cria_resposta_valida(self):
        resp = CpfResponse(valid=True, cpf="123.456.789-09", message="CPF válido")
        assert resp.valid is True
        assert resp.cpf == "123.456.789-09"
        assert resp.message == "CPF válido"

    def test_cria_resposta_invalida(self):
        resp = CpfResponse(valid=False, cpf="000.000.000-00", message="CPF inválido")
        assert resp.valid is False
