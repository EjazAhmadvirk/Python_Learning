# Check if a number is negative/positive and even/odd

num = int(input("Enter a number: "))

# Check negative or positive
if num < 0:
    print("The number is Negative.")
elif num == 0:
    print("The number is Zero.")
else:
    print("The number is Positive.")

# Check even or odd
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
