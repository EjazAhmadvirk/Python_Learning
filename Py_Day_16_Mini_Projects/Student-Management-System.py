# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("✅ Student added successfully!")

def remove_student():
    roll = input("Enter roll number to remove: ")
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("❌ Student removed successfully!")
            return
    print("⚠️ Student not found!")

def view_students():
    if not students:
        print("⚠️ No students found!")
    else:
        print("\n--- Student List ---")
        for student in students:
            print(f"Name: {student['name']} | Roll: {student['roll']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for student in students:
        if student["roll"] == roll:
            print(f"🎓 Student Found: {student['name']} (Roll: {student['roll']})")
            return
    print("⚠️ Student not found!")

def menu():
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Students")
        print("4. Search Student")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice!")

menu()
