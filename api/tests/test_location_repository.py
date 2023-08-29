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

    # Assert on the results
    assert len(locations) == 2

    assert locations == [
        Location(1, "Rad Cam", Decimal('51.750000'), Decimal('-1.250000')),
        Location(2, "Westgate", Decimal('51.750000'), Decimal('-1.260000'))
    ]

"""
When we call LocationRepository#find
We get a single a Location object reflecting seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)

    location = repository.find(2)
    assert location == Location(2, "Westgate", Decimal('51.750000'), Decimal('-1.260000'))

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
        Location(1, "Rad Cam", Decimal('51.750000'), Decimal('-1.250000')),
        Location(2, "Westgate", Decimal('51.750000'), Decimal('-1.260000')),
        Location(3, "Cornmarket", Decimal('1.111111'), Decimal('2.222222'))
    ]

"""
When we call LocationRepository#delete
We remove a record from thhe database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = LocationRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        Location(2, "Westgate", Decimal('51.750000'), Decimal('-1.260000')),
    ]