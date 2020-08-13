
# Creating first dictionary, using name, age, and city

person_0 = {'first_name': 'darius', 'last_name': 'walker', 'age': 27, 'city': 'chicago',}

print(person_0)

print("\n" + person_0['first_name'].title())
print(person_0['last_name'].title())
print(person_0[str('age')])
print(person_0['city'].title())

print(" ")
print("Example 2")
print(" ")

# Creating second dictionary, using major rivers and the country each river runs through.

countries = {'egypt': 'nile', 'brazil': 'amazon', 'china': 'yangtze',} 

for country, river in countries.items():
    print("The " + river.title() + " River runs through " + country.title() + ".")

print(" ")
print("Example 3")
print(" ")

# Creating third dictionary, dictionary within a dictionary - focused on sports teams within city

cities = {
    'dallas': {
        'football': 'cowboys',
        'baseball': 'rangers',
        'basketball': 'mavericks', 
        },
    'chicago': {
        'football': 'bears',
        'basketball': 'bulls',
        'baseball': 'sox',
        }, 
    'houston': {
        'basketball': 'rockets',
        'baseball': 'astros',
        'football': 'texans',
        }, 
    'atlanta': {
        'football': 'falcons',
        'basketball': 'hawks',
        'baseball': 'braves',
        }, 
    'denver': {
        'football': 'broncos',
        'basketball': 'nuggets',
        'baseball': 'rockies',
        },
    }

for city, sport_team in cities.items():
    print("\nCity: " + city.title())
    print("The professional football team in the area: "
     + sport_team['football'].title() + ".")
    print("The professional basketball team in the area: "
     + sport_team['basketball'].title() + ".")
    print("The professional baseball team in the area: "
     + sport_team['baseball'].title() + ".")
   

   

