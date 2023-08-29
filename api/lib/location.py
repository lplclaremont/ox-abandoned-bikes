class Location:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, latitude, longitude):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Location({self.id}, {self.name}, {self.latitude}, {self.longitude})"