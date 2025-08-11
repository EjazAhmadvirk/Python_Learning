my_set = {1, 2, 2, 3}
print(my_set)        # {1, 2, 3} (duplicates removed)
my_set.add(4)   #add element
my_set.remove(2) #remove element
my_set.clear() #clear set
print(my_set)        # set()

my_set = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set.union(my_set2) #union of sets
my_set.intersection(my_set2) #intersection of sets
my_set.difference(my_set2) #difference of sets
my_set.symmetric_difference(my_set2) #symmetric difference of sets