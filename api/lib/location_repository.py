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
        location_dict = {}  # Use a dictionary to organize rows by location_id
        for row in rows:
            location_id = row["location_id"]
            if location_id not in location_dict:
                location = self.__row_to_location(row, "location_id")
                location_dict[location_id] = {"location": location, "bikes": []}
            if row["bike_id"]:
                bike = self.__row_to_bike(row, "bike_id")
                location_dict[location_id]["bikes"].append(bike)

        locations = [data["location"] for data in location_dict.values()]
        for location_data in location_dict.values():
            location_data["location"].bikes = location_data["bikes"]
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
            bike = self.__row_to_bike(row, "bike_id")
            bikes.append(bike)

        location = self.__row_to_location(row, "location_id")
        location.bikes = bikes
        return location

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
    def __row_to_location(self, row, id="id"):
        return Location(row[id], row["name"], float(row["latitude"]), float(row["longitude"]))
    
    # Private method to convert a database row into a Bike object
    def __row_to_bike(self, row, id="id"):
        return Bike(row[id], row["brand"], row["colour"], row["condition"], row["date_found"], row["notes"], row["location_id"])
