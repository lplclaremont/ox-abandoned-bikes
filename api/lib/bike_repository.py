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
            item = Bike(row["id"], row["brand"], row["colour"], row["condition"], row["date_found"], row["location_id"])
            bikes.append(item)

        return bikes
    
    # Returns a single bike given the bike ID
    def find(self, bike_id):
        rows = self._connection.execute('SELECT * FROM bikes WHERE id = %s', [bike_id])
        row = rows[0]

        return Bike(row["id"], row["brand"], row["colour"], row["condition"], row["date_found"], row["location_id"])
    
    # Adds a new bike to the database
    def create(self, bike):
        self._connection.execute('INSERT INTO bikes (brand, colour, condition, date_found, location_id) VALUES (%s, %s, %s, %s, %s)',
                                 [bike.brand, bike.colour, bike.condition, bike.date_found, bike.location_id])
        return None
    
    # Removes bike from database given the bike ID
    def delete(self, bike_id):
        self._connection.execute('DELETE FROM bikes WHERE id = %s', [bike_id])
        return None