from flask import Flask
from lib.location_repository import LocationRepository
from lib.database_connection import DatabaseConnection
import json

app = Flask(__name__)

connector = DatabaseConnection()
connector.connect('abandoned_bikes')

@app.get("/")
def home():
    return "Hello world!"

@app.get("/locations")
def locations():
    repository = LocationRepository(connector)

    def to_json_form(location):
        return {
            "id": location.id,
            "name": location.name,
            "latitude": float(location.latitude),
            "longitude": float(location.longitude)
        }
    
    locations = list(map(to_json_form, repository.all()))
    
    return json.dumps(locations)