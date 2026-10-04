from fastapi.testclient import TestClient
from multidoc.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'What is the monthly error budget downtime?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "budget.md"
    miss = client.post("/ask", json={"question": 'soup recipe'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
