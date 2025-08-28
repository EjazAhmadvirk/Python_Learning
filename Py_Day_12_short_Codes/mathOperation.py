# Mathematics Operations in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def factorial(n):
    if n < 0:
        return "Not defined for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def square(n):
    return n * n

def cube(n):
    return n * n * n

def power(x, y):
    return x ** y


print("\n=== Mathematics Operations ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Factorial")
print("6. Square")
print("7. Cube")
print("8. Power")

choice = input("Enter choice (1-8): ")

if choice in ['1', '2', '3', '4', '8']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '8':
        print("Result:", power(num1, num2))

elif choice in ['5', '6', '7']:
    num = int(input("Enter a number: "))

    if choice == '5':
        print("Factorial:", factorial(num))
    elif choice == '6':
        print("Square:", square(num))
    elif choice == '7':
        print("Cube:", cube(num))
else:
    print("Invalid choice!")
