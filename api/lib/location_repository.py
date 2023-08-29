from .location import Location

class LocationRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
    
    # Returns a list of all locations from database
    def all(self):
        rows = self._connection.execute('SELECT * FROM locations')
        locations = []
        for row in rows:
            item = Location(row["id"], row["name"], float(row["latitude"]), float(row["longitude"]))
            print(item)
            locations.append(item)

        return locations
    
    # Returns a single location given the location ID
    def find(self, location_id):
        rows = self._connection.execute('SELECT * FROM locations WHERE id = %s', [location_id])
        row = rows[0]

        return Location(row["id"], row["name"], float(row["latitude"]), float(row["longitude"]))
    
    # Adds new location to the database
    def create(self, location):
        self._connection.execute('INSERT INTO locations (name, latitude, longitude) VALUES (%s, %s, %s)',
                                 [location.name, location.latitude, location.longitude])     
        return None
        
    # Removes location from database given the location ID
    def delete(self, location_id):
        self._connection.execute('DELETE FROM locations WHERE id = %s', [location_id])
        return None