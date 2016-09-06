# from nose import with_setup
# from app import app

import nose
import os

from context import psn

def test_index():
    client = psn.app.test_client()

    res = client.get('/')

    assert b'Hello world' in res.data
