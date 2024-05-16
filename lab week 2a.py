#NAME: ALEJANDRA SILVA

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = '10'
x = int(x)
y = 20
z = x + y
print(z)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len-1])

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z[2] = 'd'

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)


#6

color_0 = 'blue'
color = 'My favorite color is %s, what is yours?' % color_0
print(color)

#7
color_0 = 'yellow'
color = 'My favorite color is {}, what is yours?'.format(color_0)
print(color)

#8
color_0 =  'red'
color = f'My favorite color is {color_0}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools = set(schools)
schools = list(schools)
print(schools)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals_l = list(animals)
if 'dog' in animals_l:
    animals_l[animals_l.index('dog')] = 'cat'
animals = tuple(animals_l)


#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
my_sent = my_sent.lower()
letters = my_sent.split()

print(letters)
