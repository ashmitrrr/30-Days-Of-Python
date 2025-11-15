# #day 6: tuples: ordered and unchangeable, written in ( ), and once made, items cant be changed, new ones cant be added and ol ones cant be removed

# cities = ('Sydney', 'Tokyo', 'Faridabad', 'Hanoi', 'Doha', 'Singapore')
# print(type(cities)) # class tuple 
# print(len(cities)) # 3 items 

# #index

# print(cities[-1])
# print(cities[len(cities)-2])
# print(cities[-1:0:-2])

# # can be converted into a list for modifications:

# city = list(cities)
# print(type(city)) # class city

# city.append('London')
# city.append('New York')
# del city[0:6]
# cities_again = tuple(city)
# cities_merged = cities + cities_again
# print(cities_merged)
# del city
# del cities
# del cities_again

# print('It is included' if input('Enter city: ').capitalize().strip() in cities_merged else 'Not included')


# ---------------------------------------------Exercises-----------------------------------------------------

# Exercises: Level 1
# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Exercises: Level 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country




bros = ('Sam', 'Nick', 'Peter')
sis = ('Vids', 'Sera', 'Kylie')

siblings = bros + sis 
print(len(siblings))
mom_dad = ('Griffin', 'Tara')
family = mom_dad + siblings
del mom_dad
del bros
del sis
print(family)

famil_members = list(family)
print(famil_members)