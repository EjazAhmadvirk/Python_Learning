amount = int(input("Enter the amount: "))
# if amount 5000 then select this 
if amount < 5000:
    if amount < 5000 and amount > 3000:
        print("you can go to the mall")
    elif amount < 3000 and amount > 1000:
        print("you can go to the park")
    else:
        print("stay at home")
# if amount is between 5000 to 10000 then select these 
elif amount >= 5000 and amount < 10000:
    print("you can go to the Trip")
else:
    print("you can go to the vacation")
