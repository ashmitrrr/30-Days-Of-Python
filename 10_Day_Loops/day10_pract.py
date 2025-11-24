#this is day10 practise file

# while loops

count = 0
while count < 5: # here <5 is the condition
    print(count)
    count += 1

# this loops the program from 0 adding 1 until the condition is reached, which is less than 5, so it will loop from 0 to 4.

#now if:

new_count = 0
while new_count < 5: # here <5 is the condition
    print(new_count)
    new_count += 1
else:
    print(new_count)

# now in the above code, else will print the false statement after th while loop is completed, hence 5 will also be printed
# but if the while loop had ended with break, it would not go to the else loop
# else is only reached and executed if the whle loop is ran normally, not with the break


'''
BREAK AND CONTINUE
'''

# break: it is used when we wanna stop the while loop or exit it, it can also stop the loop before the initial condition is even reached

count = 0
while count < 5: # here <5 is the condition
    print(count)
    count += 1
    if count==3: # this will break the loop before 3, and the code will only return 0,1,2. it will not let it run till the condition
        break
else:
    print('While loop executed') # here the else block will not be executed as the while loop was broken, else is only executed if there is no break in the while loop

#continue: so what continue does is, unlike break which stops the loop and exits the loop completely, continue skips the current iteration
# and move to the next one

count = 0
while count < 10:
    if count==3: # here we skipped 3, and continued with the next iteration, it did not break or stopped the loop, it just skipped what we did not want
        count+=1
        continue
    print(count)
    count+=1


# for loop: it is used when we know how many times we need to loop, like we have a list or a range to loop through and u know when to stop
# while loop is when we dont know how many times we need to loop through so make it loop until a condition is reached

# in short, for loop is used to loop through a sequence, like. list, range, tuple, dict, set etc

num = [1,2,3,4,5,6,7,8,9]
for n in num:
    print(n)

# this will print the loop going through the list num

lang = 'English'
for l in lang:
    print(l)

for i in range(len(lang)):
    print(lang[i])

'''
in the above code, what happens is we take the range of len of lang, now len of lang is 7, and range of 7 is 0 to 6, as range will not count 7
we only get the numbers till 6, which will help us to get the right index
so we are printing i (index) of all the positions i that range, which is 0 to 6, so it will print the index of every letter from 0 to 6
in the word English.
'''

# for loop in dict
student = {
    "name": "Ashmit",
    "age": 20,
    "skills": ["Python", "Git", "HTML"],
}
for key, value in student.items():
    print(f"{key} has a value of {value}")

'''
BREAK & CONITNUE IN FOR LOOP
'''
# BREAK IS same as we used before

# conitnue: 

for n in range(6):
    print(n)
    if n ==3:
        continue
    print(f"Next num should be {n+1}") if n!=5 else print('Loop has ended')

else:
    print('outside')

'''
what happens here is we start a loop in range of 6, that is 0-5, and print n and then print the if else statement lines
but that print statements is only reached if it passes the n==3 condition, as soon as it will reach 3, it will skip that line and start again from top
and when n will reach 5, it will skip if and go to else, and say the loop has ended, and the it will print outside when the loop is exited.
'''

# nested for loop

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key=='skills':
        for skill in person['skills']:
            print(skill)

for n in range(10):
    print(n)
else:
    print(f"the loop stops before {n+1}") # as n will be 9 at the last iteration 


# Pass: when we have to run a code after a statement or after a :, we can use pass to simply skip the code execution
#this means we are just letting no code run where it needs a code, just to stop python to throw an error, we give it a pass
# pass helps to keep the block of code empty when needed

for i in range(9):
    pass 
#this will do NOTHING, it did not execute any code, even tho we were supposed to acc to the language, we passed it so now it wont throw an error


--------------------------------------------------EXERCISES----------------------------------------------------------------

for n in range(11):
    print(n)

n = 0
while n<11:
    print(n)
    n+=1

for n in range(10,-1,-1):
    print(n)

n = 10
while n >=0:
    print(n)
    n=n-1

start=''
for i in range(7):
    start+= '#'
    print(start)

'''
in the above one we stored an empty start variable because in that next line was depended on the last one, not needed to do in the below one as 
all are same
'''

# for row in range(7):
#     for col in range(7):
#         print('#', end =' ')
#     print()

'''
print() with nothing inside:

prints just a newline

no text, just \n

'''

for n in range(11):
    print(f'{n} x {n} = {n*n}')

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in skills:
    print(item)

for n in range(0, 101, 2):         #normwal way by skipping a place, as it will start from zero we will get even numbers
    print(n)

for n in range(101):               #using if condition to make it even
    if n %2==0:
        print(n)

for n in range(101):               #using if condition to check if its odd, and if its odd, skip it so we only get even nums
    if n%2!= 0:
        continue
    print(n)

for o in range(101):
    if o%2==0:
        continue
    print(o)

# basic easy version
total = 0
for n in range(101):
    total+= n
print(f"The sum is {total}")

# one liner

print(f"The sum is {sum(range(101))}")

total_even = 0
total_odd = 0

for n in range(101):
    if n%2==0:
        total_even+=n
    else:
        total_odd+=n
print(f"The sum of evens is {total_even} and the sum of odds is {total_odd}")

sum_even = sum(n for n in range(101) if n%2==0)
sum_odd = sum(n for n in range(101) if n%2!=0)
print(f"{sum_even} is greater than {sum_odd}")

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
]

for country in countries:
    if 'land' in country.lower():
        print(country)

print([country for country in countries if 'land' in country.lower()]) # list comprehnsion
print(*(c for c in countries if 'land' in c.lower())) # unpacking using *, because without this its just a generator list, which wont print

fruits = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruits)-1,-1,-1):
    print(fruits[i])

print([fruits[i] for i in range(len(fruits)-1, -1, -1)]) # list comprehension


