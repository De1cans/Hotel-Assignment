from classes.floors import Floor
from classes.rooms import Room

def add_floor(hotel):
    floor_id = input("Enter the id number for the new floor: ")
    floor = Floor(floor_id)
    hotel.add_floor(floor)
    print("Floor Added\n")

def list_floors(hotel):
    all_floors = hotel.get_floors()
    print("\nListing available floors...")
    if not all_floors:
        print("No floors found.")
    for floor in all_floors:
        print(floor.id)
    print("\n")

def book_room(hotel):
    booking_name = input("Enter the name of your booking: ")
    room_number = input("Enter the room number you want to book: ")
    room_to_book = Room.find_room(room_number)
    if room_to_book:
        room_booking = Room(room_number)
        if room_to_book.add_room(room_to_book):
            print("Room Booked successfully")
        else:
            print("Room is already booked out")
    else:
        print("Room does not exist")

def check_available_rooms(hotel):
    all_floors = hotel.get_floors()
    print("\nListing available floors...\n")
    if not all_floors:
        print("No floors found")
    for floor in all_floors:
        print(floor.id)
    select_floor = input("Please select a floor from the list above")