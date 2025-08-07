name = input("Enter your name: ") 
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")


"""
for simple input use input() function
for numeric input, convert the input to an integer using int() function
for floating point numbers, use float() function
means if you want to take input as a number, you can use int() or float() to convert the string input to a number


in print f is used to format the string, allowing you to include variables directly in the string using curly braces
for example, f"Hello, {name}!" will replace {name} with the value of the variable name
This is useful for creating dynamic strings that include variable values.
"""

