# Making a list immutable, "tuple"
dimensions = (400, 125)
print(dimensions[0])
print(dimensions[1])

print(" ")
print("Example 2")
print(" ")

# Looping through a tuple
dimensions = (500, 275)
for dimension in dimensions:
    print(dimension)

print(" ")
print("Example 3")
print(" ")

# Assign a new value in a tuple
dimensions = (500, 275)
print("original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (600, 315)
print("\nmodified dimensions")
for dimension in dimensions:
    print(dimension)

print(" ")
print("Example 3 remix")
print(" ")

matts_resturant = ('chicken','pork', 'beef', 'shirmp', 'tofu')
print("Matt's resturant offers:")
for matt_resturant in matts_resturant:
    print(matt_resturant)

matts_resturant = ('chicken','scallops', 'beef', 'shirmp', 'crabmeat')
print("\n Matt's new menu is:")
for matt_resturant in matts_resturant:
    print(matt_resturant)
