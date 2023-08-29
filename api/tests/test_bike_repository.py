from lib.bike_repository import BikeRepository
from lib.bike import Bike
import datetime as dt

"""
When we call BikeRepository#all
We get a list of Bike objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = BikeRepository(db_connection)

    bikes = repository.all()

    date1 = dt.datetime.strptime('2022-12-22', '%Y-%m-%d').date()
    date2 = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    date3 = dt.datetime.strptime('2022-12-24', '%Y-%m-%d').date()

    assert len(bikes) == 3
    assert bikes == [
        Bike(1, "Raleigh", "green", "poor", date1, 1),
        Bike(2, "Nigel Dean", "red", "good", date2, 2),
        Bike(3, "Dawes", "brown", "fair", date3, 2)
    ]

"""
When we call BikeRepository#find
We get a single a Bike object reflecting seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = BikeRepository(db_connection)

    bike = repository.find(2)
    date = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    assert bike == Bike(2, "Nigel Dean", "red", "good", date, 2)

"""
When we call BikeRepository#create
We create a new record in the database
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = BikeRepository(db_connection)

    repository.create(Bike(None, "Bianchi", "blue", "excellent", "2023-10-10", 1))

    result = repository.all()
    date1 = dt.datetime.strptime('2022-12-22', '%Y-%m-%d').date()
    date2 = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    date3 = dt.datetime.strptime('2022-12-24', '%Y-%m-%d').date()
    date4 = dt.datetime.strptime('2023-10-10', '%Y-%m-%d').date()

    assert result == [
        Bike(1, "Raleigh", "green", "poor", date1, 1),
        Bike(2, "Nigel Dean", "red", "good", date2, 2),
        Bike(3, "Dawes", "brown", "fair", date3, 2),
        Bike(4, "Bianchi", "blue", "excellent", date4, 1)
    ]

"""
When we call BikeRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/abandoned_bikes.sql")
    repository = BikeRepository(db_connection)
    repository.delete(1)

    result = repository.all()

    date2 = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    date3 = dt.datetime.strptime('2022-12-24', '%Y-%m-%d').date()

    assert result == [
        Bike(2, "Nigel Dean", "red", "good", date2, 2),
        Bike(3, "Dawes", "brown", "fair", date3, 2)
    ]