from . import client


def test_index():
    res = client.get('/')

    assert b'Hello world' in res.data
