from .bike import Bike

class BikeRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Returns a list of all bikes from database
    def all(self):
        rows = self._connection.execute('SELECT * FROM bikes')
        bikes = []
        for row in rows:
            bikes.append(self.__row_to_bike(row))
        return bikes
    
    # Returns a single bike given the bike ID
    def find(self, bike_id):
        rows = self._connection.execute('SELECT * FROM bikes WHERE id = %s', [bike_id])
        row = rows[0]
        return self.__row_to_bike(row)
    
    # Adds a new bike to the database
    def create(self, bike):
        self._connection.execute('INSERT INTO bikes (brand, colour, condition, date_found, notes, location_id) VALUES (%s, %s, %s, %s, %s, %s)',
                                 [bike.brand, bike.colour, bike.condition, bike.date_found, bike.notes, bike.location_id])
        return None
    
    # Updates bike in database at given the bike ID
    def update(self, bike_id, bike):
        self._connection.execute('UPDATE bikes SET brand = %s, colour = %s, condition = %s, date_found = %s, notes = %s, location_id = %s WHERE id = %s',
                                [bike.brand, bike.colour, bike.condition, bike.date_found, bike.notes, bike.location_id, bike_id])
        return None
    
    # Removes bike from database given the bike ID
    def delete(self, bike_id):
        self._connection.execute('DELETE FROM bikes WHERE id = %s', [bike_id])
        return None
    
    # Gets all bikes at a specific location
    def find_by_location_id(self, id):
        rows = self._connection.execute('SELECT * FROM bikes WHERE location_id = %s', [id])
        bikes = []
        for row in rows:
            bikes.append(self.__row_to_bike(row))
        return bikes
    
    # Private method to convert a database row into a Bike object
    def __row_to_bike(self, row):
        return Bike(row["id"], row["brand"], row["colour"], row["condition"], row["date_found"], row["notes"], row["location_id"])