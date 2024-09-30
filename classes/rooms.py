class Room():
    def __init__(self, room_number, id):
        self.room_number = room_number
        self.id = id

    def get_room_number(self):
        return self.room_number

    def get_room(self):
        return self.rooms

    def __str__(self):
        return self.room_number

    def find_room(self, room_number):
        for room in self.rooms:
            if room_number == room_number:
                return room

    def get_id(self):
        return self.id
