# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ASSIGMENT N1
#numeric
import datetime
x = 10
y = 5.1
z = x + y

print(z)

print(type(x))
print(type(y))
print(type(z))

x = 100
x +=15
print(x)

x = True
y = False

x = 10
y = 11

print(x >=y)

# string

x = "Hello world"
y = "Hello world"
z= x + y 

print(x == y)
print(z)

x += y 

print(x) # this also give us the same result

# Methods

my_string = ' hello world'
big_string = my_string.upper() #all in uppercase
print(big_string)

cap_string = my_string.capitalize() # only the 1st letter but is a space!
print(cap_string)

space_string = my_string.strip()
print(space_string)

fixed_string = my_string.strip().capitalize() # eliminate space and capitalize first
print(fixed_string)

name = 'Bob'
my_string = f'Hello {name}, welcome to class.'
print(my_string)

my_string = 'Hello {}, welcome to class.'.format(name)
print(my_string)

#another way with more control of the type 
my_string = 'Hello %s, welcome to class.' % name
print(my_string)


# Containers

## Lists

x = [1, 2, 3]
print(x)
print(len(x))

x = ['a', 'b', 'c', 'd', 'e']
print(x[1:3])
print(x[:3])
print(x[::2]) #elimina cada 2



print(x)
print(len(x))

# tupple don't hold assigments
my_tupple = ('a', 'b', 'c', 'd', 'e')
#my_tupple[0] = 'A'

#print(my_tupple)

#TypeError: 'tuple' object does not support item assignment


# set {}-> useful when we need unique values
my_set = {'a', 'b', 'a','c', 'c', 'd', 'e'}

print(my_set)

## Dictionaries
### don´t have an order

my_dict = {'a':100, 'b':200, 'c':200}
           
# So here I say position a equal to 100, B, 200, C 300.

# date time

my_date = datetime.datetime(2020, 3, 1)
print(my_date)

print(my_date.year)
print(my_date.month)


time_since_covid = datetime.datetime.now() - my_date
print(time_since_covid)