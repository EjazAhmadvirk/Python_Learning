s = {1, 2, 3}
s.add(4)        # Add element
print(s)        # {1, 2, 3, 4}
s.remove(2)     # Remove element (error if not present)
print(s)        # {1, 3, 4}
s.discard(5)    # Remove element (no error if not present)
print(s)        # {1, 3, 4}
s.pop()         # Removes a random element
print(s)        # {1, 3}
s.clear()       # Removes all elements
print(s)        # set()
