class Floor():
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_floors(self):
        return self.floors

    def add_floor(self,floor):
        self.floors.append(floor)
