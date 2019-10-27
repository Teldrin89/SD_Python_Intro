'''
# initial comment
### The Python intro repo based on sentdex introduction series ###
The Python langauge is a veristile language that can be applied to many different
applications with the only drawback beeing slightly slower than some other languages 
(like for example C)
The basic python documentation is rich enough to always start searching for specific
solution: https://docs.python.org/3/
'''

# the most basic thing a python can do is a print function
# this print function will print the text in double quotes (string)
print("Hello people!")
print("Just checking")

'''
Everything in Python is an object and some representation of that object can be a 
variable. There are some naming rules for variable (for example can't start with
a number) and the assignemnt is done with single "=" (as opposet to logical
comparison which is done with "==")
'''
food = "bread", "cheese", "ham", "tomato"

# to check the type of variable use a built in function
print(type(food))
# class of "food" variale is a tuple - immutable sequence (can be enclosed in "()")

'''
The for loop in python is an in-built function that without assignement takes a
iteration variable and performs a chunk of code repeatedly over some other variable
(eg. list)
'''
# the code run within the for loop is indentated
for typeOfFood in food:
    print(typeOfFood)
# the repeated chunk of code is a "print" function - this will printout 4 times

# the main difference between tuple and list is the immutability of tuple
otherFood = ["cucumber", "potato", "hot-dog"]
# see the different type - list - for other food which is defined with "[]"
print(type(otherFood))
# printout the other food list
for otherType in otherFood:
    print(otherType)
# within each list it is possible to put a list as variable - list of lists
game = [0,0,0,0,0,0]
# this list would be printed flat - all 6 in a line
print(game)
# to show for example a grid 3x3 it would require to use lists within the list
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# then to show the rows on top of one another use the for loop
for row in game:
    print(row)

'''
To refrence an index of a list use the "[]" and then the index number (remember 
that in Python list indexs start at "0"). To get the last index in the either use
the max index number or "-1" (first from the end). To get a range of indexes from
the list use ":" with 2 values "from" and to which "to" get the value (remembering 
that the "to" value will not be taken). To get from the begining or to the last 
use only a single value with ":".
'''
# example of list
l = [1,2,3,4,5]
# printout the list
print(l)
# printout the 2nd item from the list
print(l[1])
# printout the last item
print(l[-1])
# printout items from 2nd to 4th
print(l[1:4])
# printout indexes from 3rd to last
print(l[2:])
# the list is mutable so there is a way to change a specific values within
l[2] = 9
# check the updated list
print(l)

'''
Whenever there is a part of code in early develpment of Python script that seem
to be a repetitive but only under some different conditions use a function
instead. The PEP8 styling standards for code suggests to use small leters with
words separated by underscore, small letters at the begining for variables.
'''

# function example - an addition function
def addition(x,y):
    return x+y

# check the function work
z = addition(4,3)
print(z)

# TODO: finished on P7, 2:30