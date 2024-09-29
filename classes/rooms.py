class Room():
    def __init__(self,id):
        self.id = id

    def get_id(self):
        return self.id

    def add_room(self,room):
        self.rooms.append(room)

    def get_room_number(self):
        return self.room_number

    def __str__(self):
        return f"Room {self.room_number}"
