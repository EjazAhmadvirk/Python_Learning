#loops in Dictionary 
student = {"name": "Ejaz", "age": 21, "university": "Riphah"}

# Loop through keys
for key in student:
    print(key, ":", student[key])

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, "=>", value)
