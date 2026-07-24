import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestValidateCpfEndpoint:
    @pytest.mark.asyncio
    async def test_cpf_valido_retorna_200(self, client):
        resp = await client.post("/cpf/validate", json={"cpf": "12345678909"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is True
        assert data["cpf"] == "123.456.789-09"
        assert data["message"] == "CPF válido"

    @pytest.mark.asyncio
    async def test_cpf_valido_com_mascara(self, client):
        resp = await client.post("/cpf/validate", json={"cpf": "123.456.789-09"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is True

    @pytest.mark.asyncio
    async def test_cpf_invalido_digitos_verificadores(self, client):
        resp = await client.post("/cpf/validate", json={"cpf": "12345678900"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is False
        assert "dígito verificador" in data["message"]

    @pytest.mark.asyncio
    async def test_cpf_todos_digitos_iguais(self, client):
        resp = await client.post("/cpf/validate", json={"cpf": "11111111111"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is False

    @pytest.mark.asyncio
    async def test_cpf_tamanho_invalido_retorna_422(self, client):
        resp = await client.post("/cpf/validate", json={"cpf": "12345"})
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_body_vazio_retorna_422(self, client):
        resp = await client.post("/cpf/validate", json={})
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_campo_cpf_faltando_retorna_422(self, client):
        resp = await client.post("/cpf/validate", json={"outra_coisa": "test"})
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_metodo_incorreto_retorna_405(self, client):
        resp = await client.get("/cpf/validate")
        assert resp.status_code == 405
