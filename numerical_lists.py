# Using range() to generate a series of numbers

for value in range(1,11):
    print(value)

print(" ")
print("Example 2")
print(" ")

# Using range() to make a list of numbers
numbers = list(range(1,11))
print(numbers)

print(" ")
print("Example 3")
print(" ")

# Using range() to list specifc numbers
even_numbers = list(range(2,15,2))
print(even_numbers)

print(" ")
print("Example 4")
print(" ")

# Using the range() to generate a series of squared numbers
squares = []
for value in range(1,26):
    square = value**2
    squares.append(square)

print(squares)

print(" ")
print("or written in a more concise way.\n")

squares = []
for value in range(1,26):
    squares.append(value**2)

print(squares)

print(" ")
print("or using list comprehension.\n")

squares = [value**2 for value in range(1,26)]
print(squares)

print(" ")
print("Example 5")
print(" ")

# Simple statistics with a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(" ")


values = list(range(1, 100000001))
print(min(values))
print(max(values))
print(sum(values))


