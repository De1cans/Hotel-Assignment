class floor():
    def __init__(self, floor_number, number_of_rooms):
        self.floor_number = floor_number
        self.number_of_rooms = number_of_rooms

first_floor = floor("Floor One", "Five")
second_floor = floor("Floor Two", "Five")
third_floor = floor("Floor Three", "Five")

print(first_floor.floor_number)
print(second_floor.floor_number)
print(third_floor.floor_number)