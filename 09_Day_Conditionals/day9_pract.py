# conditions day 9 practise

# short hand style for writing conditions 

print('Even' if int(input('Enter a no. ').strip())% 2==0 else 'Odd')

                     
#nested conditions: conditions inside conditions 

a = int(input('Enter a number: ').strip())


if a > 0:
    if a % 2==0:
        print(f"{a} is a positive even number")
    else:
        print(f"{a} is a positive odd number")
elif a ==0:
    print('The number is 0.')
else:
    if a % 2==0:
        print(f"{a} is a negative even number")
    else:
        print(f"{a} is a negative odd number")


if a > 0:
    print('The number is a positive even number' if a % 2 ==0 else 'The number is a psoitive odd number') 
elif a ==0:
    print('The number is 0.') 
else: 
    print('The number is a negative even number' if a % 2 ==0 else 'The number is a negative odd number')


if a > 0:
    print(f"{a} is a positive {'even' if a % 2==0 else 'odd'} number") 
elif a ==0:
    print('The number is 0.') 
else: 
    print(f"{a} is a negative {'even' if a %2==0 else 'odd'} number")


# conditions and logical operators (and, or)

if a > 0 and a%2==0:
    print('Pos Even')
elif a > 0 and a%2!=0:
    print('Pos Odd')
else:
    print('fuck off')

user = input('Enter name: ').strip().capitalize()
access_level = int(input('enter access level: ').strip())

if user =='Admin' or access_level>4:
    print('Access granted')
else:
    print('No right to be here')

# -----------------------------------------------EXERCISES------------------------------------------

age = int(input('Enter ur age: ').strip())

if age > 18:
    print('U can drive')
else:
    print(f"U need to wait {18-age} years till u can drive")


age = int(input('Enter ur age: ').strip()); print('U can drive' if age >= 18 else f"U need to wait {18-age} year{'s' if 18-age!=1 else ''} till u can drive")

my_age = 20
your_age = int(input('Enter ur age').strip())
print('We are the same age' if my_age==your_age else f"U are {your_age-my_age} year{'s' if your_age-my_age!=1 else ''} older than me" 
      if your_age>my_age else f"U are {my_age-your_age} year{'s' if my_age-your_age!=1 else ''} younger than me")


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').strip().lower()
if fruit in fruits:
    print(f"{fruit} alredy exists in the list.")
else:
    fruits.append(fruit)
    print(f"{fruit} is added to the list, the new list is {fruits}")


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street', 'zipcode': '02210'}
}

#1) Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person and person['skills']:
    skills = person['skills']
    mid = len(skills)//2 # this is gonna give us the index of the middle item whcih will be one less than the actual middle item
    print(f"Middle skill: {skills[mid] if len(skills)%2!=0 else skills[mid-1:mid+1]}")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person and person['skills']:
    print('Python exists' if 'Python' in person['skills'] else 'Python does not exist in the list')

'''
* If a person skills has only JavaScript and React, print('He is a front end developer'), 
if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
if the person skills has React, Node and MongoDB, 
Print('He is a fullstack developer'), else print('unknown title')
 - for more accurate results more conditions can be nested!

'''

skills = set(person.get('skills', [])) # get skills key from person but if does not exist, return [] empty

if skills == {'JavaScript', 'React'}:
    print('Hes front end')
elif skills == {'Node', 'Python', 'MongoDB'}:
    print('Hes back end')
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print('Hes full stack')
else:
    print('Unknown title')
    

'''
* If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.

'''

if person['is_marred']==True and person['country']=='Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is {'married' if person['is_marred']==True else 'not married'}.")