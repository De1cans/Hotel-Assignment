from classes.hotel import Hotel

print("\n------------------------")
print("Welcome To The My Hotel!")
print("------------------------\n")

def hotel_menu():
    print("Enter 1 to see available rooms")
    print("Enter 2 to make a booking")
    print("Enter 3 to manage existing bookings")
    print("Enter 4 to skip a day")
    print("Enter 5 for Hotel Administration")
    print("Enter 6 to exit menu\n")

    choice = input("Please select a number from the list above: ")

    return choice 

choice = ""

hotel = Hotel("hotell")

while choice != "6":
    choice = hotel_menu()

    if choice == "1":
        print("You've entered 1")
    elif choice == "2":
        print("You've entered 2")
    elif choice == "3":
        print("You've entered 3")
    elif choice == "4":
        print("You've entered 4")
    elif choice == "5":
        print("You've entered 5")
    elif choice == "6":
        print("Exiting")
    else:
        print("Invalid choice")

print("\n--------------------------------")
print("Thank you for visiting the Hotel, we hope you've enjoyed your stay")
print("--------------------------------\n")