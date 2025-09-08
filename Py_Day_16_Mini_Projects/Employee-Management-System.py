# Employee Management System

employees = []

def add_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    dept = input("Enter department: ")
    employees.append({"name": name, "id": emp_id, "dept": dept})
    print("✅ Employee added successfully!")

def remove_employee():
    emp_id = input("Enter employee ID to remove: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("❌ Employee removed successfully!")
            return
    print("⚠️ Employee not found!")

def view_employees():
    if not employees:
        print("⚠️ No employees found!")
    else:
        print("\n--- Employee List ---")
        for emp in employees:
            print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['dept']}")

def search_employee():
    emp_id = input("Enter employee ID to search: ")
    for emp in employees:
        if emp["id"] == emp_id:
            print(f"👔 Employee Found: {emp['name']} (Dept: {emp['dept']})")
            return
    print("⚠️ Employee not found!")

def menu():
    while True:
        print("\n--- Employee Management ---")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. Search Employee")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice!")

menu()
