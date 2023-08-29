from flask import Flask, jsonify, request
from lib.location import Location
from lib.location_repository import LocationRepository
from lib.bike import Bike
from lib.bike_repository import BikeRepository
from lib.database_connection import DatabaseConnection

app = Flask(__name__)

connector = DatabaseConnection()
connector.connect('abandoned_bikes')

def location_to_dict(location):
    return {
        "id": location.id,
        "name": location.name,
        "latitude": location.latitude,
        "longitude": location.longitude
    }

def bike_to_dict(bike):
    return {
        "id": bike.id,
        "brand": bike.brand,
        "colour": bike.colour,
        "condition": bike.condition,
        "date_found": bike.date_found,
        "location_id": bike.location_id
    }
    
@app.get("/")
def home():
    return "Hello world!"

@app.get("/locations")
def get_locations():
    repository = LocationRepository(connector)
    locations = list(map(location_to_dict, repository.all()))
    
    return jsonify(locations), 200

@app.get("/locations/<int:location_id>")
def get_location_by_id(location_id):
    repository = LocationRepository(connector)
    location = location_to_dict(repository.find(location_id))

    return jsonify(location), 200

@app.post("/locations")
def create_location():
    data = request.get_json()
    name = data["name"]
    lat = data["latitude"]
    long = data["longitude"]

    repository = LocationRepository(connector)
    repository.create(Location(None, name, lat, long))

    return jsonify({"status": "OK"}), 200

@app.delete("/locations/<int:location_id>")
def delete_location(location_id):
    repository = LocationRepository(connector)
    repository.delete(location_id)

    return jsonify({"status": "OK"}), 200


@app.get("/bikes")
def get_bikes():
    repository = BikeRepository(connector)
    bikes = list(map(bike_to_dict, repository.all()))
    
    return jsonify(bikes), 200

@app.get("/bikes/<int:bike_id>")
def get_bike_by_id(bike_id):
    repository = BikeRepository(connector)
    location = bike_to_dict(repository.find(bike_id))

    return jsonify(location), 200

@app.post("/bikes")
def create_bike():
    data = request.get_json()
    brand = data["brand"]
    colour = data["colour"]
    condition = data["condition"]
    date_found = data["date_found"]
    location_id = data["location_id"]

    repository = BikeRepository(connector)
    repository.create(Bike(None, brand, colour, condition, date_found, location_id))

    return jsonify({"status": "OK"}), 200

@app.delete("/bikes/<int:bike_id>")
def delete_bike(bike_id):
    repository = BikeRepository(connector)
    repository.delete(bike_id)

    return jsonify({"status": "OK"}), 200