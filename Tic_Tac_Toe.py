#---------------------------------Requirements---------------------------------------------
#board
#display board
#handle turn
#check Win
    #Check win by rows
    #Check win by column
    #Check Diagonals
#check Tie
#Flip Player

#------------------------------Global  Variables---------------------------------------------------

#Game Board
board = ["-", "-", "-",
              "-", "-", "-",
                "-","-","-"]

#If a game still goes on 
if_game_is_still_going= True

#current Player
current_player = "X"

#Winner
winner= None

#Function to start the game and play Tic-Tac-Toe.
def play_game():
    
    #Displays initial board.
    display_board()

    #while the game is still going.     
    while if_game_is_still_going:
         
        #Handle the turn of the current player.
        handle_turn(current_player)

        #Checks if the game is over
        check_if_game_over()
        
        #Flips over to the next player.
        flip_player()

    #If the game is ended
    if (winner == "X" or winner == "O"):
        print(winner + " " +"Wins.")
    elif(winner== None):
        print("Tie.")


#Functoin to display the game board.
def display_board():

    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


#Handles the turn of the player.
def handle_turn(player):
    
    #Get position from player
    print(player + " 's  turn.")
    position = input("Enter your Position (1-9) :")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:
        
        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter your Position (1-9) :")

        # Get correct index in our board list
        position = int(position) - 1

         # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there")
    
    #Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()

#Check if the game is over.
def check_if_game_over():
    check_win()
    check_tie()


#Checks who won the game.
def check_win():
    # Set global variables
    global winner

    #check rows 
    row_winner = check_rows()

    
    #check columns
    column_winner= check_column()
    
    
    #check diagonal
    diagonal_winner = check_diagonal()
       
    
    #Checks winner for rows.
    if row_winner:
        winner= row_winner  


    #Checks winner for Columns.
    elif column_winner:
        winner=column_winner 


    #Check winner for Diagonal.    
    elif diagonal_winner:
        winner=diagonal_winner 
    
    else:
        winner = None
    
 

  #Check rows.
def check_rows():
    global if_game_is_still_going
    
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row1 or row2 or row3:
        if_game_is_still_going = False
    # Return the winner
    if row1:
        return board[0]
    
    elif row2:
        return board[3]
    
    elif row3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None

#Check Columns.
def check_column():
   #Set Global Variables
    global if_game_is_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
   
    # If any row does have a match, flag that there is a win
    if column1 or column2 or column3:
         if_game_is_still_going = False
        # Return the winner 
    if column1:
        return board[0]
    
    elif column2:
        return board[1]
    
    elif column3:
        return board[2]
# Or return None if there was no winner
    else:
        return None

#Checks Diagonals.
def check_diagonal():
    # Set global variables
    global if_game_is_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    
    # If any row does have a match, flag that there is a win
    if diag1 or diag2:
        if_game_is_still_going = False
    
     # If any row does have a match, flag that there is a winlif  diag1:
    if  diag1:    
        return board[0]
    
    elif diag2:
        return board[2 ]
    
    else:
        return None
    
#Checks if the game was a Tie.
def check_tie():
    #SET Global Variables
    global if_game_is_still_going
    #If board is full.
    if "-" not in board:
        if_game_is_still_going= False
        return True
    #Else there is no tie.
    else:
        return  False


#Flips over to the next player.
def flip_player():
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"
     
# ------------ Start Execution -------------
# Play a game of tic tac toe    
play_game()



    



