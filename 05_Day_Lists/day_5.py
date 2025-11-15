# # make a list

# lst = list() #empty, using list() func
# print(len(lst) ) # 0

# lst_1 = [] # empty list
# print(len(lst_1))

# # list with values
# random_list = [1, 'apple', 'HTML', True, '9', 'hello', {'name':'Ashmit', 'place': 'india'}] # various data types can be stored together
# print(f"List items: {random_list} and lenth: {len(random_list)}") # len to find out the number of items in a list

# # using index

# fruit = random_list[1] # return apple
# print(fruit)

# info = random_list[len(random_list)-1] 
# print(info)
#  # or 
# print(random_list[-2]) # hello 

# #unpacking list

# countries = ['India', 'China', 'USA', 'Canada', 'France', 'Germany', 'Austria', 'Australia', 'New Zealand']

# IN, CH, US, CA, *EU, AU, NZ = countries # very imp: in python we can only use * option ONE TIME on the left side, cant be used two stars
# ASIA = [IN, CH]
# AMERICAS = [US, CA]
# OCEANIA = [AU, NZ]

# print(f"All: {countries} and Asian: {ASIA}, America, we got {AMERICAS} and in europe we have {EU}, and the last is down under {OCEANIA}")

# # slicing 

# print(countries[::2]) # first to last skipping one in between
# print(countries[::-2]) # last to front skipping one in between 
# print(countries[2::2]) # starts from index 2 to last skipping one in between
# print(countries[::-1]) # returns all from last 

# # modifying a list

# countries[1] = 'Japan'
# countries[3] = 'Mexico'
# print(countries)

# print(True if 'India' in countries else False) # check if a item xists in the list
# print('Spain' in countries) # will also return True or false
# print('Yes' if 'China' in countries else 'No') 

# # adding and inserting= append, insert

# countries.append('Russia')
# countries.insert(3, 'Egypt') # will insert at index 3

# print(countries)

# # remove, pop, del, copy and clear

# countries.remove('Japan') # remove needs us to mention a specific name of the value
# countries.pop() # pop removes an item by addressing the item by index, and if index not mentioned, it removes the last item automatically
# countries.pop(2) # index mentioned
# del countries[3:6] # del is used to delete the whole list or group of items by index, this will delete items between 3 and 6, so items at index 4 and 5 will only be deleted
# print(countries)
# # del countries # will delete the whole list
# # print(countries) # will throw an error as it does not exist anymore

# new_countries= countries.copy() # will copy a list
# print(new_countries)

# countries.clear() # removes all the items but keeps the list
# print(countries) # will return an empty list

# countries.append('Argentina')
# countries.append('South Africa')
# countries.append('Brazil')

# # joining lists : using + and extend

# countries_plus = new_countries + countries #using plus operator, u can combine as many as u want 
# print(countries_plus)

# countries.extend(new_countries) # using .extend(), this actually appends the items of a list at the end of another list
# print(countries)

# # count : counts the number  of times a specific item appears on the list

# age = [1,2,45,21,678,32,32,32,32,5,6,8,9]
# print(age.count(32)) # 4

# print(age.index(32))  # to find out the index of an item, in case of multiple entries of the same item, it will give index of the first apperance

# # reversing a list= reverse()

# countries.reverse()
# print(countries)

# # sort and sorted

# # sort arranges the list in asc or desc order, changes the original list

# countries.sort() # by default, it will return in asc
# print(countries)

# countries_plus.sort(reverse=True) # to arrange in desc
# print(countries_plus)

# # sorted: same functionality, but gives a new list arranged in asc or desc, and keeps the original one 

# age = sorted(age, reverse=True) #desc
# print(age)


'''
---------------------------------------------------------------------------------------------------------------------------------------
'''
# EXCERCISES

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

new_list = front_end + back_end
full_stack = new_list.copy()
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age= ages[-1]
print(f"Min age: {min_age} and max age: {max_age}")
ages.append(min_age)
ages.append(max_age)
ages.sort()

# median

median = len(ages) // 2  # 12, for a list of 12 items = 6

if len(ages) % 2 ==0: # even
    print(f"Median: {(ages[(median-1)] + ages[median]) / 2}")
else: #odd
    print(ages[median])

# avg
print(f"Average : {sum(ages)/len(ages)}")

#range
print(f"Range: {max_age - min_age}")

diff_min= abs(min_age-(sum(ages)/len(ages)))
diff_max= abs(max_age-(sum(ages)/len(ages)))
print(f"Values are {diff_min} and {diff_max}. are they equal? : {diff_min==diff_max}\nis max avg bigger?: {diff_max>diff_min}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];


middle = len(countries)//2

if len(countries)%2==0:
    print(f"Middle countries are: {countries[middle-1]} and {countries[middle]}")
else:
    print(f"Middle country: {countries[middle]}")

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

print(f"First half: {countries[:((len(countries)+1)//2)]}")
print(f"Second half: {countries[((len(countries)+1)//2):]}")


example = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
CH, RU, US, *Scandic = example
print(Scandic)