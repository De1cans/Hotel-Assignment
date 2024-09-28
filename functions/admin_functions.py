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