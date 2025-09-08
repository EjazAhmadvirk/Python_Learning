# Inventory Management System

inventory = []

def add_item():
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory.append({"name": name, "qty": qty, "price": price})
    print("📦 Item added successfully!")

def remove_item():
    name = input("Enter item name to remove: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print("❌ Item removed successfully!")
            return
    print("⚠️ Item not found!")

def view_inventory():
    if not inventory:
        print("⚠️ Inventory is empty!")
    else:
        print("\n--- Inventory List ---")
        for item in inventory:
            print(f"Item: {item['name']} | Qty: {item['qty']} | Price: {item['price']}")

def search_item():
    name = input("Enter item name to search: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"✅ Item Found: {item['name']} | Qty: {item['qty']} | Price: {item['price']}")
            return
    print("⚠️ Item not found!")

def update_item():
    name = input("Enter item name to update: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            item["qty"] = int(input("Enter new quantity: "))
            item["price"] = float(input("Enter new price: "))
            print("🔄 Item updated successfully!")
            return
    print("⚠️ Item not found!")

def menu():
    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Search Item")
        print("5. Update Item")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            search_item()
        elif choice == "5":
            update_item()
        elif choice == "6":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice!")

menu()
