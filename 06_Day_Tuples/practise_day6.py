#day 6: tuples: ordered and unchangeable, written in ( ), and once made, items cant be changed, new ones cant be added and ol ones cant be removed

cities = ('Sydney', 'Tokyo', 'Faridabad', 'Hanoi', 'Doha', 'Singapore')
print(type(cities)) # class tuple 
print(len(cities)) # 3 items 

#index

print(cities[-1])
print(cities[len(cities)-2])
print(cities[-1:0:-2])

# can be converted into a list for modifications:

city = list(cities)
print(type(city)) # class city

city.append('London')
city.append('New York')
del city[0:6]
cities_again = tuple(city)
cities_merged = cities + cities_again
print(cities_merged)
del city
del cities
del cities_again

print('It is included' if input('Enter city: ').capitalize().strip() in cities_merged else 'Not included')

