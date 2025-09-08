# Hospital Management System

patients = []

def add_patient():
    name = input("Enter patient name: ")
    pid = input("Enter patient ID: ")
    disease = input("Enter disease: ")
    patients.append({"name": name, "id": pid, "disease": disease})
    print("🏥 Patient added successfully!")

def remove_patient():
    pid = input("Enter patient ID to remove: ")
    for patient in patients:
        if patient["id"] == pid:
            patients.remove(patient)
            print("❌ Patient removed successfully!")
            return
    print("⚠️ Patient not found!")

def view_patients():
    if not patients:
        print("⚠️ No patients in record!")
    else:
        print("\n--- Patient List ---")
        for p in patients:
            print(f"ID: {p['id']} | Name: {p['name']} | Disease: {p['disease']}")

def search_patient():
    pid = input("Enter patient ID to search: ")
    for p in patients:
        if p["id"] == pid:
            print(f"✅ Patient Found: {p['name']} (Disease: {p['disease']})")
            return
    print("⚠️ Patient not found!")

def update_patient():
    pid = input("Enter patient ID to update: ")
    for p in patients:
        if p["id"] == pid:
            p["name"] = input("Enter new name: ")
            p["disease"] = input("Enter new disease: ")
            print("🔄 Patient record updated successfully!")
            return
    print("⚠️ Patient not found!")

def menu():
    while True:
        print("\n--- Hospital Management ---")
        print("1. Add Patient")
        print("2. Remove Patient")
        print("3. View Patients")
        print("4. Search Patient")
        print("5. Update Patient")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            remove_patient()
        elif choice == "3":
            view_patients()
        elif choice == "4":
            search_patient()
        elif choice == "5":
            update_patient()
        elif choice == "6":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice!")

menu()
