from lib.location_repository import LocationRepository
from lib.location import Location
from decimal import Decimal


"""
When we call LocationRepository#all
We get a list of Location objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/abandoned_bikes.sql") # Seed our database with some test data
    repository = LocationRepository(db_connection) # Create a new LocationRepository

    locations = repository.all() # Get all locations


    assert len(locations) == 3
    assert locations == [
        Location(1, "Rad Cam", 51.750000, -1.250000),
        Location(2, "Westgate", 51.750000, -1.260000),
        Location(3,"Mag Bridge", 50, -1.5)
    ]

"""
When we call LocationRepository#find
We get a single a Location object reflecting seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)

    location = repository.find(2)
    assert location == Location(2, "Westgate", 51.75, -1.26)

"""
When we call LocationRepository#create
We create a new record in the database
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)

    repository.create(Location(None, "Cornmarket", 1.111111, 2.222222))

    result = repository.all()
    assert result == [
        Location(1, "Rad Cam", 51.750000, -1.250000),
        Location(2, "Westgate", 51.750000, -1.260000),
        Location(3,"Mag Bridge", 50, -1.5),
        Location(4, "Cornmarket", 1.111111, 2.222222)
    ]

"""
When we call LocationRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Location(1, "Rad Cam", 51.750000, -1.250000),
        Location(2, "Westgate", 51.750000, -1.260000),
    ]