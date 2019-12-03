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
11. Combining all of the win conditions functions for full game
12. Work on the play state - run game till winner is determined
13. Connect win function to main play state
14. Work on the "hard coded" parts of the code
15. Consider trying to use different size of the game map
16. Add a customization with colorama package

'''
import itertools, string
# prepare a game board - commented out as the starting board is down
'''
 game = [[1, 2, 2],
        [1, 1, 1],
        [2, 0, 1]]
'''
# check if numpy is installed
try:
    import numpy
except ImportError:
    print("numpy not installed")

# define a function to be called for game representation after every move
def game_board(game_map, player=0, row=0, column=0, display = False):
    try:
        # check if players are trying to play one over the other
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another")
            return game_map, False
        # print("   A  B  C") # previous look of the game map
        # new look with numbers of both axes
        # print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        # in case going back to upper case letter use string library
        print("   "+"  ".join([string.ascii_uppercase[i] for i in range(len(game_map))]))
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        print()
        return game_map, True
    # consider except condition with index error
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2", e)
        return game_map, False
    except Exception as e:
        print("Something very wrong happened!")
        return game_map, False

# define a win check function
def win(current_game):

    # new function that will check if all paramters are the same in list
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    

    # HORIZONTAL winning conditions check
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (-)!")
            # adding a return of win function
            return True
    
    # DIAGONAL winning conditions check
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True
    
    diags = []
    for ii in range(len(game)):
        diags.append(game[ii][ii])
    if all_same(diags):
        # in order print the back slash it has to be 2x\\ as the first one is the
        # special sign that says in python to treat the next character as string
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True

    # VERTICAL winning conditions check
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically (|)!")
            return True
    # at the end of the function if nobody won return false
    return False

# setup basic properties - boolean for play state and list of players
play = True
players = [1, 2]
# create a while loop that will be played till someone winns or quits
while play:
    # for start re-start a game board
    '''
    # older static game map definition
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    '''
    # start with game map size definition - by player
    game_size = int(input("What size game map do you want? " ))
    game = [[ 0 for i in range(game_size)] for i in range(game_size)]

    # setup a game won flag - False in the beggining
    game_won = False
    # show initial game map
    game, _ = game_board(game, display=True)
    # cycle temp variable for players
    player_choice = itertools.cycle(players)
    # another loop added for a specific game
    while not game_won:
        # updated - using next function cycle trough players
        current_player = next(player_choice)
        # print current player
        print(f"Current Player: {current_player}")
        # adding states - played
        played = False
        # run the current player if the turn has not been yet played
        while not played:
            # ask user about column and row - remember to put them as integers
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            # run the function and played state
            game, played = game_board(game, current_player, row_choice, column_choice)
        # add the check for if the game is won
        if win(game):
            # change game status
            game_won = True
            # ask if players want to play again
            again = input("The game is over, would you like to play again? (y/n) ")
            # check the response and execute the dedicated portions of the code
            if again.lower() == "y":
                print("Restarting....")
            elif again.lower() == "n":
                print("Ciao!")
                play = False
            else:
                print("Not a valid response, closing game!")
                play = False

'''
# check for functions working - commented out
# check if win function is working
win(game)
# check for game_board function working
game = game_board(game, display=True)
game = game_board(game, player=1, row=2, column=1)
'''