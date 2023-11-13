from lib.models.bike import Bike

"""
Bike constructs with an id, brand, colour, condition, date_found and location_id
"""
def test_bike_constructs():
    bike = Bike(1, "Test brand", "Test colour", "fair", "2023-08-25", "notes", 1)
    assert bike.id == 1
    assert bike.brand == "Test brand"
    assert bike.colour == "Test colour"
    assert bike.condition == "fair"
    assert bike.date_found == "2023-08-25"
    assert bike.notes == "notes"
    assert bike.location_id == 1


"""
We can format bikes to strings nicely
"""
def test_bikes_format_nicely():
    bike = Bike(1, "Test brand", "Test colour", "fair", "2023-08-25", "notes", 1)
    assert str(bike) == "Bike(1, Test brand, Test colour, fair, 2023-08-25, notes, 1)"


"""
We can compare two identical bikes
And have them be equal
"""
def test_bikes_are_equal():
    bike1 = Bike(1, "Test brand", "Test colour", "fair", "2023-08-25", "notes", 1)
    bike2 = Bike(1, "Test brand", "Test colour", "fair", "2023-08-25", "notes", 1)
    assert bike1==bike2
    