import pytest
from webapp import app
from flask import url_for

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"MMPI-2 Assessment Platform" in resp.data

def test_client_info_route(client):
    resp = client.get('/client_info')
    assert resp.status_code == 200
    assert b"Client Information" in resp.data or b"Client Information Entry" in resp.data

def test_score_entry_route(client):
    resp = client.get('/score_entry')
    assert resp.status_code == 200
    assert b"T-Score Entry" in resp.data or b"Enter MMPI-2 T-Scores" in resp.data

def test_view_report_redirect(client):
    resp = client.get('/view_report/nonexistent')
    # should redirect to index
    assert resp.status_code == 302
    assert resp.headers['Location'].endswith(url_for('index'))
