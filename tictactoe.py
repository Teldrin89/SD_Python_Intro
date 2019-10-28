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
def game_board(player=0, row=0, column=0, display = False):
    print("   A  B  C")
    if not display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

'''
every time the user will make a move within the game the board will have to be 
re-adjusted - hence the game_board function would have to be used so in order to
make the script easier, the game function will also be included in the function
'''
# now to change the game board, data has to be passsed to game_board function
game_board(display=True)
game_board(1,2,1)
