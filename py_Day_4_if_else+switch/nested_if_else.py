amount = int(input("Enter the amount: "))
if amount < 5000:
    if amount < 5000 and amount > 3000:
        print("you can go to the mall")
    elif amount < 3000 and amount > 1000:
        print("you can go to the park")
    else:
        print("stay at home")
elif amount >= 5000 and amount < 10000:
    print("you can go to the Trip")
else:
    print("you can go to the vacation")