# Using list and concatenation to create messages
bicycles = ['road bike', 'mountain bike', 'folding bike', 'commuter bike']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[-1].title())
print(bicycles[-2].title())

print(" ")

# Using a value from the "bicycles" list in a sentence
message = "My favorite type of bike is a " + bicycles[0].title() + "!"
print (message)
