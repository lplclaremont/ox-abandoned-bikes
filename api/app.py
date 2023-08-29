from flask import Flask, jsonify
from lib.location_repository import LocationRepository
from lib.database_connection import DatabaseConnection
import json

app = Flask(__name__)

connector = DatabaseConnection()
connector.connect('abandoned_bikes')

def to_dict_form(location):
    return {
        "id": location.id,
        "name": location.name,
        "latitude": float(location.latitude),
        "longitude": float(location.longitude)
    }
    
@app.get("/")
def home():
    return "Hello world!"

@app.get("/locations")
def get_locations():
    repository = LocationRepository(connector)

    locations = list(map(to_dict_form, repository.all()))
    
    return jsonify(locations), 200

@app.get("/locations/<int:location_id>")
def get_location_by_id(location_id):
    repository = LocationRepository(connector)

    location = to_dict_form(repository.find(location_id))

    return jsonify(location), 200