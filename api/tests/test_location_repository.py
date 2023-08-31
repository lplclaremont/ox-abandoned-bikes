from lib.location_repository import LocationRepository
from lib.location import Location
from lib.bike import Bike
import datetime as dt


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
        Location(1, "Rad Cam", 51.75, -1.25,),
        Location(2, "Westgate", 51.75, -1.26),
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
When we call LocationRepository#find_with_bikes
We get a Location object which contains a bikes array.
"""
def test_find_with_bikes(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)

    location = repository.find_with_bikes(2)

    date2 = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    date3 = dt.datetime.strptime('2022-12-24', '%Y-%m-%d').date()

    bike2 = Bike(2, "Nigel Dean", "red", "good", date2, "note2", 2)
    bike3 = Bike(3, "Dawes", "brown", "fair", date3, "note3", 2)

    assert location == Location(2, "Westgate", 51.75, -1.26, [bike2, bike3])

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
        Location(1, "Rad Cam", 51.75, -1.25),
        Location(2, "Westgate", 51.75, -1.26),
        Location(3,"Mag Bridge", 50, -1.5),
        Location(4, "Cornmarket", 1.111111, 2.222222)
    ]


"""
When we call LocationRepository#update
We change a record from the database.
"""
def test_update_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)
    new_location = Location(1, "Updated place", 55.75, -5.25)
    repository.update(1, new_location)

    result = repository.all()
    assert result == [
        Location(2, "Westgate", 51.75, -1.26),
        Location(3,"Mag Bridge", 50, -1.5),
        Location(1, "Updated place", 55.75, -5.25)
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
