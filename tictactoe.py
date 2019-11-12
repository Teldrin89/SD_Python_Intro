'''
The goal of this script is to build a game of tic-tac-toe using python and applying
some of the basic functions and modules of Python.
The best way to apporach every new project is to write down the idea in simple 
steps that can be then followed along during the creation.
# --- The Game of Tic-Tac-Toe ---
1. The basic representation of a game board will be a list of lists with size 3x3
2. The starting point will be represented by 0s and the "x" and "o" will be 
    represented by 1s and 2s (TODO: think over some functions in the future to
    represent the "x" and "o")
3. The user input will be determined by first location and then the symbol
4. Add a modification of game board - move from one of the players
5. Prepare a function that will update the game board every time it's changed
6. Update function to also take into account the turn of each players move
7. Add erorr handling options in function (for example the wrong input type)
8. Calculating one of the version of winning conditions - horizotal winner

'''

# prepare a game board
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

'''
# to change a specific position reference the index in given list of lists
game[0][1] = 1
'''
'''
# print the top row that will be column part of and adress for each position
print("   A  B  C")
'''
'''
# to lable the rows use counter - intialize counter outside of the for loop
count = 0

# print each row of the game indyvidually to get the 3x3 board
for row in game:
    # print both count and row 
    print(count, row)
    # increment count
    count += 1 # == count + 1
'''
'''
# instead of using the above code use the simpler version with in-built function
# the enumerate function will increment on iterable object - in our case rows
for count, row in enumerate(game):
    print(count, row)
'''

# define a function to be called for game representation after every move
# additional parameters passed to game_board function
# a default value of "0" added to each parameter
# adding a flag at the end for just running the code to display the game board
# update a function to pass a game_map to the game_board function
# update function for error handling: input data error
def game_board(game_map, player=0, row=0, column=0, display = False):
    # introduce error handling with try-except function
    try:
        print("   A  B  C")
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        print()
        # return a game_map
        return game_map
    # consider except condition with index error
    except IndexError as e:
        # printout message for index error
        print("Error: make sure you input row/column as 0, 1 or 2", e)
    # consider all other errors - for example programming error with wrong game 
    # map input
    except Exception as e:
        print("Something very wrong happened!")
'''
every time the user will make a move within the game the board will have to be 
re-adjusted - hence the game_board function would have to be used so in order to
make the script easier, the game function will also be included in the function
'''
# now to change the game board, data has to be passsed to game_board function
# adjust the function callout (new parameter) and assign the result to game variable
game = game_board(game, display=True)
game = game_board(game, 2,2,1)

'''
to determine the win, introduce a function that will check the current game if
the conditions for winning of the game have been met
the initial function had many flows especially the scalability of this solution
could be a problem as it is hard coded; a better solution would be to introduce
parameters that will be dynamically assigned to for example the size of game board
'''
# define a win check function - HORIZONTAL
def win(current_game):
    # check all rows in game board
    for row in game:
        # run if statement and count each row[0] - if we have the same number of
        # identical elements as a length of that row it is a winning condition
        # add exclusion of all "0" rows (starting set of game board)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("HORIZONTAL Winner!")


# check winning conditions after each update of game board
win(game)
game = game_board(game, 2,2,0)
win(game)
game = game_board(game, 2,2,2)
win(game)

# change game for vertical win conditions
game = game_board(game, 0,2,0)
game = game_board(game, 0,2,2)
game = game_board(game, 2,0,1)
game = game_board(game, 2,1,1)

# define a win check parameters - VERTICAL - using similar approach as in horizontal
# set a list variable that will be checked
check = []
# for each row in the game board append the list with 1st element of the row
for row in game:
    check.append(row[1])
# run an if statement to check the same conditions as in horizontal check but now
# on a newly defined sublist of vertical elements
if check.count(check[1]) == len(check) and check[1] != 0:
    print("VERTICAL Winner!")

# the code will only check 1st column as index is hard coded to "0" - change it to
# "1" to check the middle column