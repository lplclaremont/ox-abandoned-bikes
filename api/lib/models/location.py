class Location:    
    def __init__(self, id, name, latitude, longitude, bikes=[]):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.bikes = bikes

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Location({self.id}, {self.name}, {self.latitude}, {self.longitude}, {self.bikes})"