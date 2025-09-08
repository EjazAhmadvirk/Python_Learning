# Bank Management System

accounts = []

def create_account():
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    accounts.append({"name": name, "acc_no": acc_no, "balance": balance})
    print("🏦 Account created successfully!")

def deposit():
    acc_no = input("Enter account number: ")
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            amount = float(input("Enter deposit amount: "))
            acc["balance"] += amount
            print(f"✅ {amount} deposited! New Balance: {acc['balance']}")
            return
    print("⚠️ Account not found!")

def withdraw():
    acc_no = input("Enter account number: ")
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= acc["balance"]:
                acc["balance"] -= amount
                print(f"💸 {amount} withdrawn! New Balance: {acc['balance']}")
            else:
                print("⚠️ Insufficient funds!")
            return
    print("⚠️ Account not found!")

def check_balance():
    acc_no = input("Enter account number: ")
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            print(f"💰 Account Balance: {acc['balance']}")
            return
    print("⚠️ Account not found!")

def menu():
    while True:
        print("\n--- Bank Management ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice!")

menu()
