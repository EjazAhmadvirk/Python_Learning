from collections import namedtuple

# Define a namedtuple type
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p1 = Point(10, 20)

print(p1.x)  # Access by name → 10
print(p1[1]) # Access by index → 20
