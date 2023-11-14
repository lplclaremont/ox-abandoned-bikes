from lib.repositories.bike_repository import BikeRepository
from lib.models.bike import Bike
import datetime as dt

"""
When we call BikeRepository#all
We get a list of Bike objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    repository = BikeRepository(db_connection)

    bikes = repository.all()

    date1 = dt.datetime.strptime('2022-12-22', '%Y-%m-%d').date()
    date2 = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    date3 = dt.datetime.strptime('2022-12-24', '%Y-%m-%d').date()

    assert bikes == [
        Bike(1, "Raleigh", "green", "poor", date1, "note1", 1, "Rad Cam"),
        Bike(2, "Nigel Dean", "red", "good", date2, "note2", 2, "Westgate"),
        Bike(3, "Dawes", "brown", "fair", date3, "note3", 2, "Westgate")
    ]


"""
When we call BikeRepository#find
We get a single a Bike object reflecting seed data.
"""
def test_get_single_record(db_connection):
    repository = BikeRepository(db_connection)

    bike = repository.find(2)
    date = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()

    assert bike == Bike(2, "Nigel Dean", "red", "good", date, "note2", 2, "Westgate")


"""
When we call BikeRepository#create
We create a new record in the database
"""
def test_create_record(db_connection):
    repository = BikeRepository(db_connection)

    repository.create(Bike(None, "Bianchi", "blue", "excellent", "2023-10-10", "new note", 1))
    bikes = repository.all()
    date = dt.datetime.strptime('2023-10-10', '%Y-%m-%d').date()

    assert bikes[-1] == Bike(4, "Bianchi", "blue",
            "excellent", date, "new note", 1, "Rad Cam")


"""
When we call BikeRepository#update
We change a record from the database.
"""
def test_update_record(db_connection):
    repository = BikeRepository(db_connection)
    new_date = dt.datetime.strptime('2022-12-30', '%Y-%m-%d').date()
    new_bike = Bike(1, "Updated brand", "Updated colour", "good", new_date, "new note", 1)
    
    repository.update(1, new_bike)
    bike = repository.find(1)

    assert bike == Bike(1, "Updated brand", "Updated colour",
                        "good", new_date, "new note", 1, "Rad Cam")


"""
When we call BikeRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    repository = BikeRepository(db_connection)
    repository.delete(1)

    bikes = repository.all()

    date2 = dt.datetime.strptime('2022-12-23', '%Y-%m-%d').date()
    date3 = dt.datetime.strptime('2022-12-24', '%Y-%m-%d').date()

    assert not any (bike.id == 1 for bike in bikes)
    