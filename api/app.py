
import os
from flask import Flask, jsonify, request
from lib.location import Location
from lib.location_repository import LocationRepository
from lib.bike import Bike
from lib.bike_repository import BikeRepository
from lib.database_connection import get_flask_database_connection

app = Flask(__name__)
    
@app.get("/")
def home():
    return "Hello world!"

@app.get("/locations")
def get_locations():
    connection = get_flask_database_connection(app)
    repository = LocationRepository(connection)
    locations = [location.__dict__ for location in repository.all_with_bikes()]
    for location in locations:
        location["bikes"] = [bike.__dict__ for bike in location["bikes"]]
    
    return jsonify(locations), 200

@app.get("/locations/<int:location_id>")
def get_location_by_id(location_id):
    connection = get_flask_database_connection(app)
    repository = LocationRepository(connection)
    location = repository.find_with_bikes(location_id)
    location.bikes = [bike.__dict__ for bike in location.bikes]

    location_dict = location.__dict__

    return jsonify(location_dict), 200

@app.post("/locations")
def create_location():
    data = request.get_json()
    name = data["name"]
    lat = data["latitude"]
    long = data["longitude"]

    connection = get_flask_database_connection(app)
    repository = LocationRepository(connection)
    repository.create(Location(None, name, lat, long))

    response = {
        "status": "OK",
        "body": "location successfully added"
    }
    return jsonify(response), 200

@app.put("/locations/<int:location_id>")
def update_location(location_id):
    data = request.get_json()
    name = data["name"]
    lat = data["latitude"]
    long = data["longitude"]

    connection = get_flask_database_connection(app)
    repository = LocationRepository(connection)
    
    repository.update(location_id, Location(None, name, lat, long))

    response = {
        "status": "OK",
        "body": "location successfully updated"
    }
    return jsonify(response), 200

@app.delete("/locations/<int:location_id>")
def delete_location(location_id):
    connection = get_flask_database_connection(app)
    repository = LocationRepository(connection)
    repository.delete(location_id)

    response_data = {
        "status": "OK",
        "body": "location successfully deleted"
    }

    return jsonify(response_data), 200


@app.get("/bikes")
def get_bikes():
    connection = get_flask_database_connection(app)
    repository = BikeRepository(connection)
    bikes = [bike.__dict__ for bike in repository.all()]
    
    return jsonify(bikes), 200

@app.get("/bikes/<int:bike_id>")
def get_bike_by_id(bike_id):
    connection = get_flask_database_connection(app)
    repository = BikeRepository(connection)
    bike_dict = repository.find(bike_id).__dict__

    return jsonify(bike_dict), 200

@app.post("/bikes")
def create_bike():
    data = request.get_json()
    brand = data["brand"]
    colour = data["colour"]
    condition = data["condition"]
    date_found = data["date_found"]
    notes = data["notes"]
    location_id = data["location_id"]

    connection = get_flask_database_connection(app)
    repository = BikeRepository(connection)
    repository.create(Bike(None, brand, colour, condition, date_found, notes, location_id))

    response = {
        "status": "OK",
        "body": "bike successfully added"
    }
    return jsonify(response), 200

@app.put("/bikes/<int:bike_id>")
def update_bike(bike_id):
    data = request.get_json()
    brand = data["brand"]
    colour = data["colour"]
    condition = data["condition"]
    date_found = data["date_found"]
    location_id = data["location_id"]

    connection = get_flask_database_connection(app)
    repository = BikeRepository(connection)
    
    repository.update(bike_id, Bike(None, brand, colour, condition, date_found, location_id))

    response = {
        "status": "OK",
        "body": "bike successfully updated"
    }
    return jsonify(response), 200

@app.delete("/bikes/<int:bike_id>")
def delete_bike(bike_id):
    connection = get_flask_database_connection(app)
    repository = BikeRepository(connection)
    repository.delete(bike_id)

    response = {
        "status": "OK",
        "body": "bike successfully deleted"
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))