# Tic Tac Toe
# The things below are the conditions that is needed for the tic tac toe game:
# Will need a board
# display the board
# Play the game
# Making turns
# Check if it's a win:
    # Check the Row
    # Check the Columns
    # Check Diagonals
# Check if it's a tie
# Changing players from X player to O player


# Having a boolean statement to tell us if the game is running or not
game_is_running = True

# Having a statement telling us who the winner is
winner = None

# Having a statement to define was is the present player

presentplayer = "X"

# First creating the board
# This is just a simple list

gameboard = ["-","-","-",
             "-","-","-",
             "-","-","-"]

# Second thing is to display the game board itself
# we will be creating a display gameboard function
# need to put "|" symbol between each "-" so that we can seperate it
# Since gameboard is in a list we can call each index and add in the "|" symbol for it
# that way the board will look like the actual tic tac toe gameboard (in a sense play around with it)

def display_gameboard():
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])

# When someone wants to play tic tac toe they would want to start the game and see the board
# so this is where we would have the function to play the game
# the display gameboard function will be inside the play game function
# The play game function is going to be the main function that runs all the other functions
# now when it comes to taking a turn we want the turns to continue until the game is over right
# Therefor in order to achieve this continuation we need to put it in a loop so the game will go on forever
# While the player is taking the turn inside the loop it checks to see if the game isn't over
# If the game is not over then that means we flip the player so the next player can take their turn
# then we go back into the loop once again and go over the same process until the game is over
# Now outside the while loop we have an if statement where we compare if the winner is X or O then we print the winner
# Else if the winner is none then we print a tie

def play_game():
    display_gameboard()
    while game_is_running:
        taking_turn(presentplayer)
        game_over()
        change_player()
    if winner == "X" or winner == "O":
        print(winner + " WINS!!")
    elif winner == None:
        print("TIE")

# This is the function that lets the player take their turn
# first we want to start with a spot ie tell the player where do they want to put their X or their O
# using the input() means that it will ask it from the command line
# but in order to bring it to the board list we need to make the string into an integer ie we cast it as an int
# the reason for this is because to traverse the list we need to use the indexes which are integer
# since index start with 0 we need to subtract by 1 so it would be accurate
# Once the spot has been chosen now we need to place it on the board itself
# We choose X because X always goes first
# and then display the board with the new result
# Error Handling:
# if you chose other number besides 1-9 u will get an invalid spot
# if the gameboard spot is "-" then you are good but if it isn't valid then it will say the spot is take chose another one

def taking_turn(player):
    print(player + "'s Turn")
    spot = input("Choose the spot which is ranged from 1 to 9: ")
    valid = False
    while not valid:
        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("Invalid Spot!! Choose the spot which is ranged from 1 to 9: ")
        spot = int(spot) - 1
        if gameboard[spot] == "-":
            valid = True
        else:
            input("Spot is already taken. Chose another one.")
    gameboard[spot] = player
    display_gameboard()

# creating the game over function
# this function pretty much has 2 functions inside of this function
# win function or tie function

def game_over():
    win()
    tie()

# This function describes how to check who won the game
# To win a game we need to check if there are 3 in a row, 3 in a column, or 3 in diagonal
# So in this function we got 3 more functions inside one for row, one for column, one for diagonal
# defined the global variable winner inside the fuction so that it can be written to the variable outside
# we set the win conditions to the row, column, and diagonal functions
# if there is 3 in a row we get the winner, else if column is 3 we get a winner, else if diagonal is 3 we get a winner
# else there is no winner

def win():
    global winner
    row_three = rows()
    column_three = columns()
    diagonal_three = diagonals()
    if row_three:
        winner = row_three
    elif column_three:
        winner = column_three
    elif diagonal_three:
        winner = diagonal_three
    else:
        winner = None
    return

# This is the function that tells the game its a tie
# first have game is running global variable
# For the game to be a tie it means all the pieces spots needs to be filled up
# in that case we just need to make sure there is no "-" in the gameboard meaning it filled up and it should work since its a list
# if "-" is not in the gameboard then stop the game

def tie():
    global game_is_running
    if "-" not in gameboard:
        game_is_running = False
    return

# This function will change players after their turn is made
# Define global varable presentplayer in this function
# If the present player is X then it is changed to O after it takes its turn
# Else if the present player is O then it is changed to X after it takes its turn

def change_player():
    global presentplayer
    if presentplayer == "X":
        presentplayer = "O"
    elif presentplayer == "O":
        presentplayer = "X"

    return

# This is the function that checks if the rows has a match ie 3 in a row
# defining the global variable for game is running to match it outside of this function
# to check if we have 3 in a row we need to see if each element on the gameboard is the same
# the gameboard is a list so the element is in the index
# since there are only 3 rows we can say that if the index 0-2 are the same and isn't a "-" then that is row1
# the same logic applies to row2 and row3
# If any of the 3 rows are a match then that means we stop the game because someone won
# To get which player actually won based on the row we just have to match the first element of a row
# since the other 2 elements in that row will be the same there won't be any need to check them
# ie if the first element in row 1 is X then that means X won because it got 3 in a row

def rows():
    global game_is_running
    row1 = gameboard[0] == gameboard[1] == gameboard[2] != "-"
    row2 = gameboard[3] == gameboard[4] == gameboard[5] != "-"
    row3 = gameboard[6] == gameboard[7] == gameboard[8] != "-"
    if row1 or row2 or row3:
        game_is_running = False
    if row1:
        return gameboard[0]
    elif row2:
        return gameboard[3]
    elif row3:
        return gameboard[6]
    return

# This is the function that checks if the columns has a match ie 3 in a column
# defining the global variable for game is running to match it outside of this function
# to check if we have 3 in a column we need to see if each element on the gameboard is the same
# the gameboard is a list so the element is in the index
# since there are only 3 columns we can say that if the index 0,3,6 are the same and isn't a "-" then that is column1
# the same logic applies to column2 and column3
# If any of the 3 columns are a match then that means we stop the game because someone won
# To get which player actually won based on the column we just have to match the first element of a column
# since the other 2 elements in that column will be the same there won't be any need to check them
# ie if the first element in column 1 is X then that means X won because it got 3 in a column

def columns():
    global game_is_running
    column1 = gameboard[0] == gameboard[3] == gameboard[6] != "-"
    column2 = gameboard[1] == gameboard[4] == gameboard[7] != "-"
    column3 = gameboard[2] == gameboard[5] == gameboard[8] != "-"
    if column1 or column2 or column3:
        game_is_running = False
    if column1:
        return gameboard[0]
    elif column2:
        return gameboard[1]
    elif column3:
        return gameboard[2]
    return

# This is the function that checks if the diagonals has a match ie 3 in a diagonal
# defining the global variable for game is running to match it outside of this function
# to check if we have 3 in a diagonal we need to see if each element on the gameboard is the same
# the gameboard is a list so the element is in the index
# since there are only 2 diagonals we can say that if the index 0,4,8 are the same and isn't a "-" then that is diagonal1
# the same logic applies to diagonal2
# If any of the 3 diagonals are a match then that means we stop the game because someone won
# To get which player actually won based on the diagonal we just have to match the first element of a diagonal
# since the other 2 elements in that diagonal will be the same there won't be any need to check them
# ie if the first element in diagonal 1 is X then that means X won because it got 3 in a diagonal

def diagonals():
    global game_is_running
    diagonal1 = gameboard[0] == gameboard[4] == gameboard[8] != "-"
    diagonal2 = gameboard[2] == gameboard[4] == gameboard[6] != "-"
    if diagonal1 or diagonal2:
        game_is_running = False
    if diagonal1:
        return gameboard[0]
    elif diagonal2:
        return gameboard[2]
    return

play_game()