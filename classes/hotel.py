class Hotel():
    def __init__(self, name):
        self.name = name 
        self.floors = []

    def add_floor(self, floor):
        self.floors.append(floor)

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    