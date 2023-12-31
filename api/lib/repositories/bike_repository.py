from ..models.bike import Bike

class BikeRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Returns a list of all bikes from database
    def all(self):
        query = '''
            SELECT bikes.id, bikes.brand, bikes.colour, bikes.condition,
                bikes.date_found, bikes.notes, locations.id as location_id, locations.name as location_name
            FROM bikes JOIN locations
            ON locations.id = bikes.location_id
            ORDER BY bikes.id
        '''
        rows = self._connection.execute(query)
        bikes = [self.__row_to_bike(row) for row in rows]

        return bikes
    
    # Returns a single bike given the bike ID
    def find(self, bike_id):
        query = '''
            SELECT bikes.id, bikes.brand, bikes.colour, bikes.condition,
                bikes.date_found, bikes.notes, locations.id as location_id, locations.name as location_name
            FROM bikes JOIN locations
            ON locations.id = bikes.location_id
            WHERE bikes.id = %s
        '''

        rows = self._connection.execute(query, [bike_id])
        bike = self.__row_to_bike(rows[0])
        
        return bike
    
    # Adds a new bike to the database
    def create(self, bike):
        query = '''
            INSERT INTO bikes (brand, colour, condition, date_found,
            notes, location_id) VALUES (%s, %s, %s, %s, %s, %s)
        '''
        params = [bike.brand, bike.colour, bike.condition, bike.date_found,
                  bike.notes, bike.location_id]
        self._connection.execute(query, params)

        return None
    
    # Updates bike in database at given the bike ID
    def update(self, bike_id, bike):
        query = '''
            UPDATE bikes SET brand = %s, colour = %s, condition = %s,
            date_found = %s, notes = %s, location_id = %s WHERE id = %s
        '''
        params = [bike.brand, bike.colour, bike.condition, bike.date_found,
                  bike.notes, bike.location_id, bike_id]
        self._connection.execute(query, params)
        
        return None
    
    # Removes bike from database given the bike ID
    def delete(self, bike_id):
        self._connection.execute('DELETE FROM bikes WHERE id = %s', [bike_id])
        return None
    
    # Private method to convert a database row into a Bike object
    def __row_to_bike(self, row):
        return Bike(row["id"], row["brand"], row["colour"], row["condition"],
                row["date_found"], row["notes"], row["location_id"], row["location_name"])