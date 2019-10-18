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
for type_of_food in food:
    print(type_of_food)
# the repeated chunk of code is a "print" function - this will printout 4 times

# the main difference between tuple and list is the immutability of tuple
other_food = ["cucumber", "potato", "hot-dog"]
# see the different type - list - for other food which is defined with "[]"
print(type(other_food))
# printout the other food list
for other_type in other_food:
    print(other_type)
# within each list it is possible to put a list as variable - list of lists
game = [0,0,0,0,0,0]
# this list would be printed flat - all 6 in a line
print(game)
# to show for example a grid 3x3 it would require to use lists within the list
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# then to show the rows on top of one another use the for loop
for row in game:
    print(row)
