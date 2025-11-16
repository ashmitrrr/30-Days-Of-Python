# #day 7 practise

# # SETS: unordered, unindexed and every item is different, it is used to store distinct elements, denoted by { }

# numbers = {1, 45, 35, 35, 0, 9, 76, 89}
# print(type(numbers)) # set
# print(numbers)   # will only give 35 once

# print(45 in numbers)

# # add() and update()
# # add can only add one item to the set at a time, update can add multiple elements in the set at a time in the form for a list argument

# numbers.add(100)
# numbers.update([101, 109, 150]) # takes a list argument [ ]. 
# print(numbers)

# # fyi: sets may not return the numbers in a same order as sets are unordered and the result might be in a different order

# #remove() and pop()

# numbers.remove(100) # removes the mentioned element
# numbers.pop() # removes any random number from the set
# removed_number= numbers.pop()
# print(removed_number)
# print(numbers)

# # del and clear
# numbers.clear()
# print(numbers)
# del numbers

# # unions and update (joining sets)

# #union joins and returns a new set

# st1 = {1,2,3,4,5}
# st2 = {6,7,8,9,10}
# st3 = st1.union(st2)
# print(st3)

# # update: does not return a new set, it simply udpates the previous set to combine two sets

# st1.update(st2)
# print(st1)
# del st3

# # intersection: to find out the common elements in two sets
# print(st1.intersection(st2)) # 6,7,8,9,10

# # subsets and supersets

# # subsets : issubset(); super set: issuperset()

# print(st2.issubset(st1)) # true as all elements of set 2 are a part of set 1
# print(st1.issuperset(st2)) # true again as set 1 is the superset of set 2

# cat = {'c', 'a', 't'}
# mat = {'m','a','t'}
# print(cat.union(mat)) # c,a,t,m union wont return repeated letters
# print(cat.intersection(mat)) # a,t only common letters
# print('Yes' if cat.issubset(mat) else 'No') # No as not all the letters of mat are in cat 

# # difference

# print(cat.difference(mat)) # will give c, not m, as the difference is asked from cat
# print(mat.difference(cat)) # will give m
# print(st1.difference(st2))

'''
=======================Exercises===========================

'''

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# A.update(B)
# print(A)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A
del B
age_st = set(age)
print(type(age_st))
print('List is bigger than set' if len(age)>len(age_st) else 'Set is bigger')

str = "I am a teacher and I love to inspire and teach people.". split()
st = set(str)
print(st)
print(len(st))