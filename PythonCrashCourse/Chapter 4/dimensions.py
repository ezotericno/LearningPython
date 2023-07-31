# Tuples are a list of items that cannot change (immutable)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through all values in a tuple

for dimension in dimensions:
  print(dimension)

# Tuples cannot be changed but they can be overwritten
dimensions = (400, 100)
# this new line would be fine within the code because the tuple is reassigned properly
