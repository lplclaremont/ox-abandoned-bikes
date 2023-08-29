from lib.location import Location

class LocationRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM locations')
        locations = []
        for row in rows:
            item = Location(row["id"], row["name"], row["latitude"], row["longitude"])
            locations.append(item)

        return locations