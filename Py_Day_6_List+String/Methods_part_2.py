# Creating a list
my_list = [3, 1, 2, 3]



# pop()
my_list.pop()  # Removes last → [3, 1, 2, 3, 4, 5]

# index()
print(my_list.index(3))  # 0 (first occurrence of 3)

# count()
print(my_list.count(3))  # 2 (number of 3s)

# sort()
my_list.sort()  # [1, 2, 3, 3, 4, 5]

# reverse()
my_list.reverse()  # [5, 4, 3, 3, 2, 1]

# copy()
new_list = my_list.copy()

# clear()
my_list.clear()  # []
