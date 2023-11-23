#step1
def evaluate(board):
  "This function accepts the string with the board of 1D tic-tac-toe as argument and returns one character based on the state of the game"
  board_length = len(board)
  for x in board:
    if "xxx" in board:
      print("The player who uses crosses (Xs) has won!")
      return "x"
    elif "ooo" in board:
      print("The player who uses noughts (Os) has won!")
      return "o"
    elif board_length > 20:
      print("The board is full, nobody won!")
      return "!"
    else:
      print("Contunue playing!")
      return "-"

#step2
def move(board, mark, position):
  "This function returns the game board with the given mark in the given position."
  if board[position] != " ":
        return "Position is already taken."

  new_board = board[:position] + mark + board[position+1:]
  return new_board

#step3
def player_move(board):
  "This function accepts a string with the game board, asks the player which position he wants to play and returns the updated game board with the player's move and checks if values are correct."
  player_position = int(input("Choose postion of your mark (0-19):"))

  if board[player_position] == " ":
    if player_mark == "x" and player_position >=0 and player_position <20:
      new_board = board[:player_position] + player_mark + board[player_position+1:]
      return new_board

    elif player_mark == "o" and player_position >= 0 and player_position <20:
      new_board = board[:player_position] + player_mark + board[player_position+1:]
      return new_board

    else:
      print("Invalid position or mark, try again.")
      return player_move(board)

  else:
    print("This spot is taken, choose another!")
    return player_move(board)
  
 #step 4
from random import randrange

def pc_move(board):
  "This function returns a game board with the computer's move."
  # loop until a valid move is found
  while True:
        pc_position = randrange(0,19)
        # check if the position is empty
        if board[pc_position] == " ":
            # replace the position with the mark and return the new board
            new_board = board[:pc_position] + pc_mark + board[pc_position+1:]
            return new_board


#step5
def oneD_tictactoe():
    # create an empty board
    board = "                    "
    print(board)
    # loop until the game is over
    while True:
        # let the player make a move
        board = player_move(board)
        print(board)
        # check the status 
        status = evaluate(board)
        if status != "-":
            break
        # let the computer make a move
        board = pc_move(board)
        print(board)
        # check the status
        status = evaluate(board)
        if status != "-":
            break
    # print the final status of the game
    print(status)

#step6: run the code

print("Welcome 1-Dimensional Tic-tac-toe game!")

player_mark = str(input("What sign would you like to use: x or o?"))
if player_mark == "x" or "o":
  if player_mark == "x":
    pc_mark = "o"
  else:
    pc_mark = "x"
else:
  print("Invalid mark, choose 'x' or 'o'")
  player_mark = str(input("What sign would you like to use: x or o?"))

oneD_tictactoe()