from lib.location import Location

"""
location constructs with an id, name, latitude and longitude
"""
def test_location_constructs():
    location = Location(1, "Test location", 1.0, 2.0)
    assert location.id == 1
    assert location.name == "Test location"
    assert location.latitude == 1.0
    assert location.longitude == 2.0

"""
We can format locations to strings nicely
"""
def test_locations_format_nicely():
    location = Location(1, "Test location", 1.0, 2.0)
    assert str(location) == "Location(1, Test location, 1.0, 2.0)"
    # Try commenting out the `__repr__` method in lib/location.py
    # And see what happens when you run this test again.

"""
We can compare two identical locations
And have them be equal
"""
def test_locations_are_equal():
    location1 = Location(1, "Test location", 1.0, 2.0)
    location2 = Location(1, "Test location", 1.0, 2.0)
    assert location1 == location2
    # Try commenting out the `__eq__` method in lib/location.py
    # And see what happens when you run this test again.