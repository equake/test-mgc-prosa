import pytest
from pydantic import ValidationError

from app.models.cnpj import CnpjRequest, CnpjResponse


class TestCnpjRequest:
    def test_cnpj_puro_funciona(self):
        data = CnpjRequest(cnpj="11222333000181")
        assert data.cnpj == "11222333000181"

    def test_cnpj_com_mascara_e_normalizado(self):
        data = CnpjRequest(cnpj="11.222.333/0001-81")
        assert data.cnpj == "11222333000181"

    def test_mascara_alternativa(self):
        data = CnpjRequest(cnpj="11 222 333 / 0001 - 81")
        assert data.cnpj == "11222333000181"

    def test_menos_de_14_digitos_lanca_erro(self):
        with pytest.raises(ValidationError):
            CnpjRequest(cnpj="12345")

    def test_mais_de_14_digitos_lanca_erro(self):
        with pytest.raises(ValidationError):
            CnpjRequest(cnpj="1234567890123456")

    def test_string_vazia_lanca_erro(self):
        with pytest.raises(ValidationError):
            CnpjRequest(cnpj="")

    def test_apenas_pontuacao_lanca_erro(self):
        with pytest.raises(ValidationError):
            CnpjRequest(cnpj=".../----")

    def test_cnpj_com_letras_e_normalizado(self):
        with pytest.raises(ValidationError):
            CnpjRequest(cnpj="abcde")


class TestCnpjResponse:
    def test_cria_resposta_valida(self):
        resp = CnpjResponse(valid=True, cnpj="11.222.333/0001-81", message="CNPJ válido")
        assert resp.valid is True
        assert resp.cnpj == "11.222.333/0001-81"
        assert resp.message == "CNPJ válido"

    def test_cria_resposta_invalida(self):
        resp = CnpjResponse(valid=False, cnpj="00.000.000/0000-00", message="CNPJ inválido")
        assert resp.valid is False
