from flask import Flask, jsonify, request
from lib.location_repository import LocationRepository
from lib.location import Location
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