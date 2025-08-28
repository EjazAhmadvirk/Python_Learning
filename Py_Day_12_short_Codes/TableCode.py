# Multiplication Table in Python

num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
