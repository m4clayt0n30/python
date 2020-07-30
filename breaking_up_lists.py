# Slicing a list

basketball_players = ['jordan', 'lebron', 'kobe', 'westbrook', 'hardin', 'magic', 'bird', 'curry']
print(basketball_players[0:3])
print(basketball_players[1:4])
print(basketball_players[2:5])
print(basketball_players[:7])
print(basketball_players[3:])
print(basketball_players[-6:])

print(" ")
print("Example 2")
print(" ")

# Looping through a slice

print("These players are considered legends: ")
for basketball_player in basketball_players[:4]:
    print(basketball_player.title())

print(" ")
print("Example 3")
print(" ")

# Copying a list
my_favorite_colors = ['blue', 'brown', 'red']
my_son_favorite_colors = my_favorite_colors[:]

print("My favorite colors are:")
print(my_favorite_colors)

print("\nMy son's favorite colors are:")
print(my_son_favorite_colors)

print(" ")
print("Example 4")
print(" ")

# Modifying the copied lists individually
my_favorite_colors.append('black')
my_son_favorite_colors.append('green')

print("My favorite colors are:")
print(my_favorite_colors)

print("\nMy son's favorite colors are:")
print(my_son_favorite_colors)
