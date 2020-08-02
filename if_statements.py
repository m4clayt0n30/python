# First if_else statement

colors = ['blue', 'green', 'red', 'brown', 'gold', 'silver']

for color in colors:
    if color == 'brown':
        print("I do not like " + color + " shoes!")
    else:
        print("I love " + color + " shoes!")

print(" ")
print("Example 2")
print(" ")

# Using if statment to check for inequality

requested_shoe_color = ["gold"]

if requested_shoe_color != 'brown':
    print("Nice choice, I am glad you didn't ask for brown shoes.")

print(" ")
print("Example 3")
print(" ")

# Checking to see if a value is not in a list

available_colors = ['blue', 'green', 'red', 'brown', 'gold', 'silver']
color = 'black'

if color not in available_colors:
    print("I'm sorry, we don't have that color available!")

print(" ")
print("Example 4")
print(" ")

# Numerical Comparison

age = 23

if age >= 20:
    print("You are old enough to get into the club.")
else:
    print("Sorry, your are not old enough.")

print(" ")
print("Example 5")
print(" ")

# Making a if-elif-else statement

weight_in_lbs = 175

if weight_in_lbs <= 30:
    print("Sorry, you are too little for this ride.")
elif weight_in_lbs >= 250:
    print("Sorry, you are too heavy for this ride.")
else:
    print("Have fun on the ride!")

print(" ")
print("Or")
print(" ")

age = 13

if age <= 5:
    price_for_slice_of_pizza = 2
elif age <= 10:
    price_for_slice_of_pizza = 5
elif age <= 18:
    price_for_slice_of_pizza = 7
else:
    price_for_slice_of_pizza = 10

print("Your costs for a slice of pizza is $" + str(price_for_slice_of_pizza) + ".")


print(" ")
print("Example 6")
print(" ")

# Testing Multiple Conditions

stage_of_life = ['baby', 'toddler', 'kid', 'teenager', 'adult', 'elder']

age = 23

if age < 2:
    stage_of_life = 'baby'
elif age < 4:
    stage_of_life = 'toddler'
elif age < 13:
    stage_of_life = 'kid'
elif age < 20:
    stage_of_life = 'teenager'
elif age < 65:
    stage_of_life = "adult"
else:
    stage_of_life = "elder"

print("The person is a (or an) " + stage_of_life + ".")

print(" ")
print("Example 7")
print(" ")

# If statements with lists

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + "st")
    elif ordinal_number == 2:
        print(str(ordinal_number) + "nd")
    elif ordinal_number ==3:
        print(str(ordinal_number) + "rd")
    else:
        print(str(ordinal_number) + "th")
