from lib.models.location import Location
from lib.repositories.location_repository import LocationRepository
from lib.models.bike import Bike
from lib.repositories.bike_repository import BikeRepository
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect('abandoned_bikes_test')
bike_repo = BikeRepository(connection)

print(bike_repo.all())