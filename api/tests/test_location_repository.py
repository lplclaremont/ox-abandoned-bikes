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