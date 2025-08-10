import array as arr

# Creating an integer array
my_array = arr.array('i', [1, 2, 3, 4])  # 'i' means signed integer

# Adding an element
my_array.append(5)

# Removing an element
my_array.remove(2)

print(my_array)  # array('i', [1, 3, 4, 5])
