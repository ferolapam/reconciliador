from fastapi.testclient import TestClient
from app.service import app
from app.schemas import Invoice

client = TestClient(app)


def test_health():
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json() == {'status': 'ok'}


def test_reconcile_match_and_unmatched():
    a = [{'id': 'inv-1', 'amount': 100.0}, {'id': 'inv-2', 'amount': 50.0}]
    b = [{'id': 'inv-1', 'amount': 100.0}, {'id': 'inv-3', 'amount': 60.0}]
    res = client.post('/reconcile', json={'source_a': a, 'source_b': b})
    assert res.status_code == 200
    body = res.json()
    assert len(body['matched']) == 1
    assert len(body['unmatched_a']) == 1
    assert len(body['unmatched_b']) == 1
