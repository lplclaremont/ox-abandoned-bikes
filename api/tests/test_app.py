from flask import json


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
    assert data[0] == {
        "id": 1,
        "name": "Rad Cam",
        "latitude": 51.75,
        "longitude": -1.25,
        "bikes": [{
            "id": 1,
            "brand": "Raleigh",
            "colour": "green",
            "condition": "poor",
            "date_found": "Thu, 22 Dec 2022 00:00:00 GMT",
            "notes": "note1",
            "location_id": 1,
            "location_name": None  
        }]
    }

    assert data[1]["name"] == "Westgate"
    assert data[2]["name"] == "Mag Bridge"


"""
Test GET /locations/id returns a single location
"""
def test_get_single_location(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    response = web_client.get("/locations/1")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data == {
        "id": 1,
        "name": "Rad Cam",
        "latitude": 51.75,
        "longitude": -1.25,
        "bikes": [
            {
                "id": 1,
                "brand": "Raleigh",
                "colour": "green",
                "condition": "poor",
                "date_found": "Thu, 22 Dec 2022 00:00:00 GMT",
                "notes": "note1",
                "location_id": 1,
                "location_name": None   
            }
        ]
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
        "longitude": 2.5,
        "bikes": []
    }

    assert data[-1] == expected_location


"""
PUT /locations/id updates the location at given ID
"""
def test_put_locations(web_client, db_connection):
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
        "longitude": 2.5,
        "bikes": [
            {"id": 1,
            "brand": "Raleigh",
            "colour": "green",
            "condition": "poor",
            "date_found": "Thu, 22 Dec 2022 00:00:00 GMT",
            "notes": "note1",
            "location_id": 1,
            "location_name": None}
        ]
    }


"""
DELETE /locations/id deletes the location at given ID
"""
def test_delete_locations(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")

    response = web_client.delete("/locations/3")

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "OK"
    assert data["body"] == "location successfully deleted"

    response = web_client.get("locations")
    data = json.loads(response.data)

    assert len(data) == 2
    assert not any(location["id"] == 3 for location in data)


"""
test GET /bikes returns bikes in JSON form
"""
def test_get_bikes(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    response = web_client.get("/bikes")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data) == 3
    assert data[0] == {
        "id": 1,
        "brand": "Raleigh",
        "colour": "green",
        "condition": "poor",
        "date_found": "Thu, 22 Dec 2022 00:00:00 GMT",
        "notes": "note1",
        "location_id": 1,
        "location_name": "Rad Cam"
    }

    assert data[1]["brand"] == "Nigel Dean"
    assert data[2]["brand"] == "Dawes"


"""
Test GET /bikes/id returns a single bikes
"""
def test_get_single_bike(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    response = web_client.get("/bikes/2")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data == {
        "id": 2,
        "brand": "Nigel Dean",
        "colour": "red",
        "condition": "good",
        "date_found": "Fri, 23 Dec 2022 00:00:00 GMT",
        "notes": "note2",
        "location_id": 2,
        "location_name": "Westgate"
    }


"""
POST /bikes adds a new bike to the database
"""
def test_post_new_bike(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")

    response = web_client.post("/bikes", json={
        "brand": "New bike",
        "colour": "blue",
        "condition": "poor",
        "date_found": "2023-08-10",
        "notes": "note",
        "location_id": 1
    })

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "OK"
    assert data["body"] == "bike successfully added"

    response = web_client.get("/bikes")
    data = json.loads(response.data)

    expected_bike = {
        "id": 4,
        "brand": "New bike",
        "colour": "blue",
        "condition": "poor",
        "date_found": "Thu, 10 Aug 2023 00:00:00 GMT",
        "notes": "note",
        "location_id": 1,
        "location_name": "Rad Cam"
    }

    assert expected_bike in data


"""
PUT /bikes/id updates the location at given ID
"""
def test_put_bikes(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")

    response = web_client.put("/bikes/1", json={
        "brand": "New bike",
        "colour": "blue",
        "condition": "poor",
        "date_found": "Thu, 10 Aug 2023 00:00:00 GMT",
        "notes": "new note",
        "location_id": 1
    })

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "OK"
    assert data["body"] == "bike successfully updated"

    response = web_client.get("bikes/1")
    data = json.loads(response.data)

    assert data == {
        "id": 1,
        "brand": "New bike",
        "colour": "blue",
        "condition": "poor",
        "date_found": "Thu, 10 Aug 2023 00:00:00 GMT",
        "notes": "new note",
        "location_id": 1,
        "location_name": "Rad Cam"
    }


"""
DELETE /bikes/id deletes the bike at given ID
"""
def test_delete_bikes(web_client, db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")

    response = web_client.delete("/bikes/3")

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "OK"
    assert data["body"] == "bike successfully deleted"

    response = web_client.get("/bikes")
    data = json.loads(response.data)

    assert len(data) == 2
    assert not any(bike["id"] == 3 for bike in data)
    