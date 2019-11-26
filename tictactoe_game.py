'''
The goal of this script is to build a game of tic-tac-toe using python and applying
some of the basic functions and modules of Python.
The best way to apporach every new project is to write down the idea in simple 
steps that can be then followed along during the creation.
# --- The Game of Tic-Tac-Toe ---
1.  The basic representation of a game board will be a list of lists with size 3x3
2.  The starting point will be represented by 0s and the "x" and "o" will be 
     represented by 1s and 2s (TODO: think over some functions in the future to
     represent the "x" and "o")
3.  The user input will be determined by first location and then the symbol
4.  Add a modification of game board - move from one of the players
5.  Prepare a function that will update the game board every time it's changed
6.  Update function to also take into account the turn of each players move
7.  Add erorr handling options in function (for example the wrong input type)
8.  Calculating one of the version of winning conditions - horizotal winner
9.  Calculating one of the version of winning conditions - veritcal winner
10. Calculating one of the version of winning conditions - diagonal winner
11. Combining all of the functions for full game
12. Work on user input

'''

# prepare a game board
game = [[1, 2, 2],
        [1, 1, 1],
        [2, 0, 1]]


# define a function to be called for game representation after every move
def game_board(game_map, player=0, row=0, column=0, display = False):
    try:
        print("   A  B  C")
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        print()
        return game_map
    # consider except condition with index error
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2", e)
    except Exception as e:
        print("Something very wrong happened!")

# define a win check function
def win(current_game):
    # HORIZONTAL winning conditions check
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally (-)!")
    
    # DIAGONAL winning conditions check
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/)!")
    
    diags = []
    for ii in range(len(game)):
        diags.append(game[ii][ii])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        # in order print the back slash it has to be 2x\\ as the first one is the
        # special sign that says in python to treat the next character as string
        print(f"Player {diags[0]} is the winner diagonally (\\)!")

    # VERTICAL winning conditions check
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[col]) == len(check) and check[col] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")
# setup basic properties - boolean for play state and list of players
play = True
players = [1, 2]
# create a while loop that will be played till someone winns or quits
while play:
    # for start re-start a game board
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    # setup a game won flag - False in the beggining
    game_won = False
    # show initial game map
    game = game_board(game, display=True)
    # another loop added for a specific game
    while not game_won:
        # for now set player
        current_player = 1
        # ask user about column and row - remember to put them as integers
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        # run the function
        game = game_board(game, current_player, row_choice, column_choice)

'''
# check for functions working - commented out
# check if win function is working
win(game)
# check for game_board function working
game = game_board(game, display=True)
game = game_board(game, player=1, row=2, column=1)
'''