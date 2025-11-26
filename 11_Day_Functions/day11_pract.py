#this is day 11

def sum_a_b():
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    print(f"Sum: {a+b}")

sum_a_b()

#using return

def full_name():
    first = 'Ashmit'
    last = 'Raina'
    full = first + ' ' + last
    return full
print(full_name())

def calc(num1, num2):
    total = num1 + num2
    diff = num1-num2
    prod = num1*num2
    div = num1//num2
    return total, diff, prod, div

print(calc(10,5))

'''
now by default, the above code will return a tuple, for example it will give me (15,5,50,2). this is a tuple. by default return will always 
give us many values in a tuple, now if we want a cleaner verison see below:
'''

def calc(num1, num2):
    total = num1 + num2
    diff = num1-num2
    prod = num1*num2
    div = num1//num2
    return f"The sum is {total}", f"The diff is {diff}", f"The product is {prod}", f"The floor division is {div}"

'''
we always need commas to seperate in return as return will give us a tuple
'''
for line in calc(10,5):
    print(line)

'''
now here we unpack the tuple using a for loop, we print line by line a single line seperating them from the comma, so easy

now the second method is to unpack the tuple: 
'''

def calc(num1, num2):
    total = num1 + num2
    diff = num1-num2
    prod = num1*num2
    div = num1//num2
    return total, diff, prod, div

total, diff, prod, div = calc(9,3)
print(f"total is {total}\ndiff is {diff}\nproduct is {prod}\nthe divison is {div}")
