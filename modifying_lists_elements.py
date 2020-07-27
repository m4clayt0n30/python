# Modifying lists in various ways
print("Example 1")
print(" ")

# Creating a list
car_brands = ['kia', 'honda', 'toyota', 'dodge', 'ford']
print(car_brands)

print(" ")
print("Example 2")
print (" ")

# Replacing kia with lexus
car_brands[0] = 'lexus'
print(car_brands)

print(" ")
print("Example 3")
print (" ")

# Readding kia to the end of the list
car_brands.append('kia')
print(car_brands)

print(" ")
print("Example 4")
print (" ")

# Adding items to an empty list
clothing_brands = []
clothing_brands.append('nike')
clothing_brands.append('reebok')
clothing_brands.append('adidas')
print(clothing_brands)

print(" ")
print("Example 5")
print (" ")

# Inserting an item into a list
clothing_brands.insert(1,'puma')
print(clothing_brands)

print(" ")
print("Example 6")
print (" ")

# Removing an item from a list
del clothing_brands[2]
print(clothing_brands)

print(" ")
print("Example 7")
print (" ")

# Removing an item from the clothing_brands list using the pop() method
popped_clothing_brands = clothing_brands.pop()
print(clothing_brands)
print(popped_clothing_brands)

print(" ")
print("Example 8")
print (" ")

# Creating a statement from an item stored in the popped_clothing_brands list
do_not_own = popped_clothing_brands
print("The only pair of shoes I don't currently own is " + do_not_own.title() + ".")

print(" ")
print("Example 9")
print (" ")

# Creating a statement from pop() to remove an item in a list at a specific position
favorite_brand = clothing_brands.pop(0)
print("My favorite clothing brand is " + favorite_brand.title() + ".")

print (" ")
print("Example 10")
print (" ")

# Removing a specific value from a list
car_brands_2 = ['kia', 'honda', 'toyota', 'dodge', 'ford', 'nissan', 'hyundai', 'suzuki']
print(car_brands_2)

car_brands_2.remove('dodge')
print(car_brands_2)

print (" ")
print("Example 11")
print (" ")

# Removing a specific value from a list and providing a reason
not_foreign = 'ford'
car_brands_2.remove(not_foreign)
print(car_brands_2)
print("I can't drive a " + not_foreign.title() + ", I only drive foreign cars.")

print(" ")
print("Example 12")
print(" ")

# Sorting a list alphabetically and reverse alphabetically
cities = ['chicago', 'dallas', 'atlanta', 'houston', 'denver', 'brooklyn', 'seattle']
cities.sort()
print(cities)

print(" ")
cities.sort(reverse=True)
print(cities)


print(" ")
print("Example 13")
print(" ")

# Temporarily sorting list 

print("Here is the original list:")
print(cities)

print(" ")
print("Here is the sorted list:")
print(sorted(cities))

print(" ")
print("Here is the original list again:")
print(cities)

print(" ")
print("Example 14")
print(" ")

# Reversing the order of a list
print(cities)
print(" ")
print("Here is the same list in reverse order")
cities.reverse()
print(cities)

print(" ")
print("Example 15")
print(" ")

# Finding the length of a list
print(cities)
print(" ")
print(len(cities))

