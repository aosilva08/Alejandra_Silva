# PPHA 30537
# Spring 2024
# Homework 1

# ALEJANDRA SILVA
# aosilva08

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

start_list = [2, 3, 4, 6, 8, 9]

for item in start_list: 
        print("The value at position", start_list.index(item) ," is", item)  


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

import re


example_list = [ "radar", "A man, a plan, a canal, Panama!", "Microsoft", "This isn't a palindrome"]

for string in example_list:
    mod_string = re.sub("[!,%& ]","",string.lower().strip())
    if mod_string[::-1] == mod_string:
         result = True
         print(result)
    else:
         result = False
         print(result)


# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.

available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')

while choice not in available_vegetables:
    print("the user can´t have the vegetable")
    choice = input('Please pick a vegetable I have available: ')
print("The vegetable is available")



# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

list1 = ["Alejandra", "Ximena", "Guille"]
list2 = ["Alberto", "Joaquin", "Diego"]


new_list = [x.lower() for x in list1 if x.lower()[0] not in ("a","b") ] 
print(new_list)

# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

new_dict = { short_names[i]: long_names[i] for i in range(0,len(short_names))}

print(new_dict)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def question_2_1(arg1,arg2):
    sum_arg= arg1 +arg2
    if sum_arg > 10:
       result = "big"
    elif sum_arg == 10:
       result = "just right"
    else:
        result = "small"    
    return result


fin_list = [ question_2_1(list(start_list[i])[0],list(start_list[i])[1] ) for i in range(0,len(start_list)) ]
   
print(fin_list)

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()
print(x)

def new_my_func(a):
    b = 40
    return a + b

x = new_my_func(10)   
print(x)

#Why new_my_func is better than my_func? Having the argument a in "new_my_func"
# allow us to tailor our calculation without needing to store a global variable

# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
import random
import string


def my_password(length, special_chars=True, numbers=True):
    if length < 8 or length > 16:
        return "Warning: The length is not between 8 and 16."
    
    chars = string.ascii_letters 
    if numbers:
        chars += string.digits  
    if special_chars:
        chars += "!@#$%^&*()"  
        
    password = ''  
    for _ in range(length):
        password += random.choice(chars)  
    
    return password




print(my_password(12))  
print(my_password(10, special_chars=False))  
print(my_password(15, numbers=False, special_chars=False))  
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

class MovieDatabase():
    def __init__(self,person):
        self.person = person
        self.movies = []

    def add_movie(self,name_movie,genera_movie, rating_movie):
        if rating_movie<0:
            print("Rating must be between 0 to 5")
        if rating_movie>5:
            print("Rating must be between 0 to 5")
        else :            
            self.movies.append(
                [name_movie, genera_movie, rating_movie]
                           )
    def what_to_watch(self):         
        if self.movies:  
            index = random.randint(0, len(self.movies) - 1)
            random_pick = self.movies[index] 
            print(f"Tonight's recommendation of {self.person} is to watch {random_pick[0]} - Genre: {random_pick[1]}, Rating: {random_pick[2]}")
        else:
            print("No movies for tonight")


inst1 = MovieDatabase("Alejandra")
inst1.add_movie("Titanic", "Drama",5)
inst1.add_movie("Narnia", "Fantasy",4)
inst1.add_movie("Hobit", "Fantasy",1)
inst1.add_movie("E.T", "Fantasy",5)
inst1.what_to_watch()

