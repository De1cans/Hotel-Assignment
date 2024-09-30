from classes.hotel import Hotel
from functions.hotel_functions import book_room, check_available_rooms, add_floor

print("\n------------------------")
print("Welcome To The My Hotel!")
print("------------------------\n")

def hotel_menu():
    print("Enter 1 to see available rooms")
    print("Enter 2 to make a booking")
    print("Enter 3 to manage existing bookings")
    print("Enter 4 to skip a day")
    print("Enter 5 for exit menu\n")

    choice = input("Please select a number from the list above: ")

    return choice 

choice = ""

hotel = Hotel("hotell")

while choice != "5":
    choice = hotel_menu()

    if choice == "1":
        check_available_rooms(hotel)
    elif choice == "2":
        book_room(hotel)
    elif choice == "3":
        print("You've entered 3")
    elif choice == "4":
        add_floor(hotel)
    elif choice == "5":
        print("Exiting")
    else:
        print("Invalid choice")

print("\n--------------------------------")
print("Thank you for visiting the Hotel, we hope you've enjoyed your stay")
print("--------------------------------\n")