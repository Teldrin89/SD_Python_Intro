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

'''
This function works for numbers put as parameters but also works for example for
2 strings - when they have "+" sign in between it works as concatenate but when
using for example "2" and "apple" it wont work because these would be 2 different
variable formats. The blessing and a curse of Python is that it doesn't need a
variable type set but it require user to know what type of parameters have to be
provided to function.
'''

'''
Mutability and immutability of some variables may have crucial role in script 
writing.
'''

# set a variable - string
game = "I want to play a game"
# print the game variable
print(game)
# check the id of game variable
print(id(game))

# set a simple function that will try to change the game variable
def game_change():
    game = "A game"
    # print the game variable from function
    print(game)
    # print the id value of game variable
    print(id(game))

# run game_change
game_change()
# check for the updated game variable
print(game)
# game variable was not changed with function script
# print the game id
print(id(game))

'''
The results show that there are 2 variables of the same name but that are actually
2 different variables - hence one was set at the begining and the other comes from
game_change() function. When trying something similar with list of numbers the
function will allow to update the values within a list but not to change it's 
content with different type of data (eg. string)
'''

# set a variable - list
game_list = [1, 2, 3]
# print the game list and it's ID
print(game_list)
print(id(game_list))

# prepare a function that will change the content of game_list variable
def game_update():
    # try to update the game variable with change to string
    # game_list = "A game"

    # try to update just a value within list
    game_list[1] = 56
    # printout the variable and it's ID
    print(game_list)
    print(id(game_list))

# run the function
game_update()
# printout the game_list (with ID)
print(game_list)
print(id(game_list))

'''
Now with that latest version of the game_update it is possible to modify the value
within the list of variable that was referenced before function and still reference
to it after function execution.
'''

'''
A quiz - guess by commenting the print line of each question the value of x 
'''

x = 1
def test():
    x = 2
test()
print(x) # 1


x = 1
def test1():
    global x
    x = 2
test1()
print(x) # 2


x = [1]
def test2():
    x = [2]
test2()
print(x) # [1]


x = [1]
def test3():
    global x
    x = [2]
test3()
print(x) # [2]


x = [1]
def test4():
    x[0] = 2
test4()
print(x) # [2]
print()
'''
For the general way to implement error handling it's best to use the "try: except:"
formula that will try the piece of code and in case of an error we can return 
information back to user. Apart form "try" and "except" there are additional 
options within this function as "else" and "finally"
'''

'''
In order to filp between 2 items inside a list there are a few ways to do that:
one would be to run a loop in which the items inside the list are
'''
# list to run back and forth through
players = [1,0]
# added a temp variable
choice = 1
for i in range(10):
    # set the current player as choice + 1
    current_player = choice + 1
    # print the current player
    print(current_player)
    # change the choice temp value to the index in players of choice
    choice = players[choice]

print()
'''
The other way to make this rotating list would be to use some built in functions
or external libraries - such as itertools
'''
# import the library
import itertools
# prepare a variable that will be generated by cycle function  of itertools (1, 2)
player_choice = itertools.cycle([1, 2])
# run the same loop to 10 to check the results
for i in range(10):
    print(next(player_choice))
