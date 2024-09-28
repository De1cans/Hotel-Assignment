from classes.hotel import Hotel
from functions.admin_functions import add_floor, list_floors

print("\n------------------------")
print("Welcome To The My Hotel!")
print("------------------------\n")

def hotel_menu():
    print("Enter 1 to see available rooms")
    print("Enter 2 to make a booking")
    print("Enter 3 to manage existing bookings")
    print("Enter 4 to skip a day")
    print("Enter 5 for Hotel Administrator")
    print("Enter 6 to exit menu\n")

    choice = input("Please select a number from the list above: ")

    return choice 

choice = ""

hotel = Hotel("hotell")

def admin_menu():
    print("Enter 1 to add floors")
    print("Enter 2 to list floors")
    print("Enter 3 to add rooms")
    print("Enter 4 to list rooms")
    print("Enter 5 to return to hotel menu")

    admin_choice = input("Please select a number from the list above: ")

    return admin_choice

admin_choice = ""

while choice != "6":
    choice = hotel_menu()

    if choice == "1":
        list_floors(hotel)
    elif choice == "2":
        add_floor(hotel)
    elif choice == "3":
        print("You've entered 3")
    elif choice == "4":
        print("You've entered 4")
    elif choice == "5":
        admin_menu()
    elif choice == "6":
        print("Exiting")
    else:
        print("Invalid choice")

while admin_choice != "5":
    admin_choice = admin_menu()

    if admin_choice == "1":
        list_floors(hotel)
    elif admin_choice == "2":
        add_floors(hotel)
    elif admin_choice == "3":
        print("Admin choice 3")
    elif admin_choice == "4":
        print("Admin choice 4")
    elif admin_choice == "5":
        hotel_menu()

print("\n--------------------------------")
print("Thank you for visiting the Hotel")
print("--------------------------------\n")