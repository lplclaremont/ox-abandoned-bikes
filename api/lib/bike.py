class Bike:
    def __init__(self, id, brand, colour, condition, date_found, notes, location_id, location_name=None):
        self.id = id
        self.brand = brand
        self.colour = colour
        self.condition = condition
        self.date_found = date_found
        self.notes = notes
        self.location_id = location_id
        self.location_name = location_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Bike({self.id}, {self.brand}, {self.colour}, {self.condition}, {self.date_found}, {self.notes}, {self.location_id})"
