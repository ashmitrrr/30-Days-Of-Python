# Arithmetic Operations in Python
# Integers
'''
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

'''

# cal area of circle 
'''
radius = float(input('Enter radius: '))
print(f'Area: {3.14 * (radius ** 2)}')
'''
# cal weight
'''
mass = float(input('Enter mass:'))
print(f'Weight = {mass * 9.81}N')
'''

# print(3 > 2)
# print(2>3)
# print(len('ashmit')!=len('vidhita'))
# print(True == False)
# print(True != True)

"""
-----------------------EXERCISES------------------------------------

"""

# 4-6 concepts area and perimeter of triangle

# height = float(input('Enter height of triangle:'))
# base = float(input('Enter base of triangle:'))
# side_a = float(input('Enter side of triangle:'))
# side_b = float(input('Enter second side of triangle:'))

# print(f'Area: {0.5 * height * base} and Perimeter: {side_a+ side_b+base}')

# cal slope and distance between two points 
# x1 = float(input('Enter x1 :'))
# y1 = float(input('Enter y1 :'))
# x2 = float(input('Enter x2 :'))
# y2 = float(input('Enter y2 :'))
# print(f'Slope m : {(y2-y1)/(x2-x1)} and distance: {((x2-x1)**2 + (y2-y1)**2)**0.5}')

'''
Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at what x value y is going to be 0.

'''
# def f(x):
#     return x**2 + 6*x +9

# for x in [-5,-4,-3,-2,-1,0]:
#     print(f'x: {x} and y: {f(x)}')
#     if f(x) == 0:
#         print('y is 0 here')
#         break
    
'''
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course not is not full of jargon. Use in operator to check if jargon is not in the sentence.

'''

# print(f"Len of python: {len('python')} and Len of dragon: {len('dragon')}\n and are their len not same: {len('python')!=len('dragon')}")
# print(f"{'on' in 'python' and 'on' in 'dragon' or 'jargon' not in 'I hope this course is not full of jargon'}")

'''
Write a Python script that displays the following table

'''
# for n in range(1,6):
#     print(n, 1, n, n**2, n**3)

'''
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10 (wrong, will throw error, value is float)
'''

# print(f"{(7 // 3)==(int(2.7))}")
# print(type('10')==type(10))
# print(float(9.8)==10)



