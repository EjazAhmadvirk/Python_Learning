import time
import os

# Car details
car_details = {
    "A": ("Ferrari 2019", 3000),
    "B": ("Hyundai 2019", 4000),
    "C": ("Honda 2019", 5000),
    "D": ("Ford 2019", 6000),
    "E": ("Toyota 2019", 7000)
}

# Customer structure (using dictionary instead of struct)
customer = {
    "name": "",
    "carmodel": "",
    "cnic": ""
}

# Welcome function
def welcome():
    print("\n\n\t\t\tWelcome To Car Rental System")
    time.sleep(1)
    print("\n\n\t\t\tStarting the program please wait...")
    time.sleep(2)
    print("\n\n\t\t\tLoading up files...")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

# Login function
def login():
    try:
        with open("My PBL Work.txt", "r") as f:
            file_password = f.readline().strip()
    except FileNotFoundError:
        print("Error: Password file not found!")
        return

    while True:
        print("\n\n\t\t\tCAR RENTAL SYSTEM")
        print("\t\t\t------------------------------")
        print("\t\t\tLOGIN")
        print("\t\t\t------------------------------\n")
        input_password = input("Enter Password: ")

        if input_password == file_password:
            print("\n\t\t\tAccess granted ✅")
            input("Press Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("\n\t\t\tAccess Aborted ❌")
            input("Press Enter to try again...")
            os.system("cls" if os.name == "nt" else "clear")

# Show car details
def show_car_details(carmodel):
    os.system("cls" if os.name == "nt" else "clear")
    if carmodel in car_details:
        print(f"You selected: {car_details[carmodel][0]}")
    else:
        print("Invalid car model!")

# Calculate rent
def calculate_rent(carmodel, days):
    print("\nCalculating rent, please wait...")
    time.sleep(2)
    if carmodel in car_details:
        return days * car_details[carmodel][1]
    else:
        return 0

# Show invoice
def show_invoice(customer, days, rental_fee):
    carmodel_name = car_details[customer["carmodel"]][0]
    print("\n                  Car Rental - Customer Invoice")
    print("   /////////////////////////////////////////////////////////////")
    print(f"   | Invoice No.          |{'cbn123':>15}   |")
    print(f"   | Customer Name        |{customer['name']:>15}   |")
    print(f"   | Customer CNIC        |{customer['cnic']:>15}   |")
    print(f"   | Car Model            |{carmodel_name:>15}   |")
    print(f"   | No of Days           |{days:>15}   |")
    print(f"   | Total Rent           |{rental_fee:>15}   |")
    print(f"   | Caution Money        |{'0':>15}   |")
    print(f"   | Advance              |{'0':>15}   |")
    print("   ------------------------------------------------------------")
    print(f"   | Total Rental Amount  |{rental_fee:>15}   |")
    print("   ------------------------------------------------------------")
    print("   # This is a computer-generated slip, it does not")
    print("     require an authorized signature #")
    print("   /////////////////////////////////////////////////////////////")
    print("   You are advised to pay the amount before the due date")
    print("   Otherwise penalty fee will be charged")
    print("   /////////////////////////////////////////////////////////////\n")
    input("Press Enter to exit...")

# Main program
def main():
    os.system("cls" if os.name == "nt" else "clear")
    welcome()
    login()

    customer["name"] = input("Please Enter Your Name: ")
    while True:
        print("\nSelect a car model:")
        print("Press A for Ferrari 2019")
        print("Press B for Hyundai 2019")
        print("Press C for Honda 2019")
        print("Press D for Ford 2019")
        print("Press E for Toyota 2019")
        carmodel = input("Enter choice: ").upper()

        if carmodel in car_details:
            customer["carmodel"] = carmodel
            show_car_details(carmodel)
            break
        else:
            print("Invalid choice! Try again.\n")
            time.sleep(1)

    customer["cnic"] = input("Enter your CNIC: ")

    while True:
        try:
            days = int(input("Enter number of days you want to rent the car: "))
            if days > 0:
                break
            else:
                print("Days must be positive!")
        except ValueError:
            print("Invalid input! Enter a valid number.")

    rental_fee = calculate_rent(customer["carmodel"], days)
    show_invoice(customer, days, rental_fee)

if __name__ == "__main__":
    main()
