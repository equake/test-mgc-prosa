import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestValidateCnpjEndpoint:
    @pytest.mark.asyncio
    async def test_cnpj_valido_retorna_200(self, client):
        resp = await client.post("/cnpj/validate", json={"cnpj": "11222333000181"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is True
        assert data["cnpj"] == "11.222.333/0001-81"
        assert data["message"] == "CNPJ válido"

    @pytest.mark.asyncio
    async def test_cnpj_valido_com_mascara(self, client):
        resp = await client.post("/cnpj/validate", json={"cnpj": "11.222.333/0001-81"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is True

    @pytest.mark.asyncio
    async def test_cnpj_invalido_digitos_verificadores(self, client):
        resp = await client.post("/cnpj/validate", json={"cnpj": "11222333000100"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is False
        assert "dígito verificador" in data["message"]

    @pytest.mark.asyncio
    async def test_cnpj_todos_digitos_iguais(self, client):
        resp = await client.post("/cnpj/validate", json={"cnpj": "11111111111111"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["valid"] is False

    @pytest.mark.asyncio
    async def test_cnpj_tamanho_invalido_retorna_422(self, client):
        resp = await client.post("/cnpj/validate", json={"cnpj": "12345"})
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_body_vazio_retorna_422(self, client):
        resp = await client.post("/cnpj/validate", json={})
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_campo_cnpj_faltando_retorna_422(self, client):
        resp = await client.post("/cnpj/validate", json={"outra_coisa": "test"})
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_metodo_incorreto_retorna_405(self, client):
        resp = await client.get("/cnpj/validate")
        assert resp.status_code == 405
