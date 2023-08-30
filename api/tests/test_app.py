from flask import json

from lib.database_connection import DatabaseConnection

"""
test GET / returns Hello world!
"""
def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello world!"

"""
test GET /locations returns locations in JSON form
"""
def test_get_locations(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    response = web_client.get("/locations")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data) == 3