from .location import Location
from .bike import Bike

class LocationRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
    
    # Returns a list of all locations from database
    def all(self):
        rows = self._connection.execute('SELECT * FROM locations')
        locations = []
        for row in rows:
            locations.append(self.__row_to_location(row))
        return locations
    
    def all_with_bikes(self):
        query = '''
            SELECT locations.id as location_id, locations.name, locations.latitude, locations.longitude,
                bikes.id AS bike_id, bikes.brand, bikes.colour, 
                bikes.condition, bikes.date_found, bikes.notes
            FROM locations
            LEFT JOIN bikes ON locations.id = bikes.location_id
        '''
        rows = self._connection.execute(query)
        locations = []
        # Iterate through rows beginning with the index 0
        i = 0
        while i < len(rows):
            bikes = []
            current_row = rows[i]
            # Create a location for current row
            location = Location(current_row["location_id"], current_row["name"],
                     float(current_row["latitude"]), float(current_row["longitude"]))
            # Now populate bikes array with data from the rows and stop when next row is different location
            while i < len(rows) and rows[i]["location_id"] == current_row["location_id"]:
                if rows[i]["bike_id"]:
                    bike = Bike(rows[i]["bike_id"], rows[i]["brand"], rows[i]["colour"],
                            rows[i]["condition"], rows[i]["date_found"], rows[i]["notes"], rows[i]["location_id"])
                    bikes.append(bike)
                # Increment i to go to next row
                i += 1
            location.bikes = bikes
            locations.append(location)
        return locations

    # Returns a single location given the location ID
    def find(self, location_id):
        rows = self._connection.execute('SELECT * FROM locations WHERE id = %s', [location_id])
        row = rows[0]
        return self.__row_to_location(row)
    
    # Returns a single location with bikes array
    def find_with_bikes(self, location_id):
        query = '''
            SELECT locations.id as location_id, locations.name, locations.latitude, locations.longitude,
                   bikes.id AS bike_id, bikes.brand, bikes.colour, bikes.condition, bikes.date_found, bikes.notes
            FROM locations
            JOIN bikes ON locations.id = bikes.location_id
            WHERE locations.id = %s
        '''
        rows = self._connection.execute(query, [location_id])
        bikes = []

        for row in rows:
            bike = Bike(row["bike_id"], row["brand"], row["colour"],
                        row["condition"], row["date_found"], row["notes"], row["location_id"])
            bikes.append(bike)

        return Location(row["location_id"], row["name"], float(row["latitude"]), float(row["longitude"]), bikes)

    # Adds new location to the database
    def create(self, location):
        self._connection.execute('INSERT INTO locations (name, latitude, longitude) VALUES (%s, %s, %s)',
                                 [location.name, location.latitude, location.longitude])     
        return None
        
    # Updates location in database at given the location ID
    def update(self, location_id, location):
        self._connection.execute('UPDATE locations SET name = %s, latitude = %s, longitude = %s WHERE id = %s',
                                [location.name, location.latitude, location.longitude, location_id])
        return None

    # Removes location from database given the location ID
    def delete(self, location_id):
        self._connection.execute('DELETE FROM locations WHERE id = %s', [location_id])
        return None
    
    # Private method to convert a database row into a Location object
    def __row_to_location(self, row):
        return Location(row["id"], row["name"], float(row["latitude"]), float(row["longitude"]))
    
