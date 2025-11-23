# # DAY 8 practise 

# # Dictionaries: we use { } to store items in a dictionary
# empty = {} # an empty dict

# # creating a dictionary:


# print(info)

# # addresing dictionary items by key 

# print(f"Name of the person: {info['name']} and age: {info['age']}")

# # changing the value of the key

# info['age'] = 21
# print(info)

# # checking keys if they exist
# print('email' in info)


# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# person.pop('first_name')        # Removes the firstname item
# person.popitem()                # Removes the address item
# del person['age']    


# print(person)


# more practise 

# info = {

#     'name':'Ashmit',
#     'last_name':'Raina',
#     'age': 20,
#     'occupation': 'Student',
#     'skills': ['python', 'data analytics', 'AI']
# }

# print(info.get('gpa', 'N/A')) # key missing in dict but get wont raise a error but give a default value 'None', or anything else if mentioned like N/A
# print(info.get('name')) # will return Ashmit

# # add a new key and value to the dict
# info["uni"] = 'UTS'

# info['skills'].append('Sql') # append to a mutated list in the dict

# freequency count  (char) very important 

# basic if else version

'''
word = input('Enter a text: ')
freq = {}

for c in word:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)
'''

# using get function

# text = input('Enter a text: ').strip().replace(' ', '')
# freq = {}

# for c in text:
#     freq[c] = freq.get(c, 0) + 1

# print(freq)

# freequency count  (word)

# sent = input('Enter a sentence: ').split()
# freq = {}

# for w in sent:
#     freq[w] = freq.get(w, 0) + 1
# print(freq)

# do the same with import Counter

from collections import Counter; sent = input('Enter a sentence: ').split(); freq = Counter(sent); print(freq)

