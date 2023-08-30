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
    assert data[0]["name"] == "Rad Cam"
    assert data[0]["latitude"] == 51.75
    assert data[0]["longitude"] == -1.25
    assert data[1]["name"] == "Westgate"
    assert data[2]["name"] == "Mag Bridge"

"""
Test GET /location/id returns a single location
"""
def test_get_single_location(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    response = web_client.get("/locations/2")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data == {
        "id": 2,
        "name": "Westgate",
        "latitude": 51.75,
        "longitude": -1.26
    }

"""
POST /locations adds a new location to the database
"""
def test_post_locations(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")

    response = web_client.post("/locations", json={
        "name": "New Location",
        "latitude": 1.5,
        "longitude": 2.5
    })

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "OK"
    assert data["body"] == "location successfully added"

    response = web_client.get("/locations")
    data = json.loads(response.data)

    expected_location = {
        "id": 4,
        "name": "New Location",
        "latitude": 1.5,
        "longitude": 2.5
    }

    assert any(location == expected_location for location in data)

"""
PUT /locations/id updates the location at given ID
"""
def test_post_locations(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")

    response = web_client.put("/locations/1", json={
        "name": "New Location",
        "latitude": 1.5,
        "longitude": 2.5
    })

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "OK"
    assert data["body"] == "location successfully updated"

    response = web_client.get("locations/1")
    data = json.loads(response.data)

    assert data == {
        "id": 1,
        "name": "New Location",
        "latitude": 1.5,
        "longitude": 2.5
    }
