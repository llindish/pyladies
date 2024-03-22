#Pyladies Project 2 - Battleship

import random

#function to draw battleship board grid and ships
def draw_battleship_map(coordinates):

  grid = [['.'] * 10 for i in range(10)]

  # Place ships at the given coordinates
  for x, y in coordinates:
    grid[x][y] = 'X'
    
  # Print the grid
  for row in grid:
    print(row) 

#function for player to choose locations of their ships
def player_ship_locations():
  list_of_coords = []                 #create an empty list
  for ship in range(1,6):             #limits the drawing to 6 ships

    while True:

      x = int(input("Enter the 'x' coordinate of your ship " + str(ship) +": ")) #ask for x coordinate input
      y = int(input("Enter the 'y' coordinate of your ship " + str(ship) +": ")) #ask for y coordinate input

      if x < 0 or x > 9 or y < 0 or y > 9 :         #test if both coordinates are within the expexted range (0-9)
        print("Wrong coordinates. Please choose x&y betweeen 0 and 9.")
      elif (x,y) in list_of_coords:                 #test if the coordinate pair is not already taken
        print("This spot is already taken, please choose different x&y.")
      else:
        list_of_coords.append((x, y))               #all good - combine x&y and add to the list
        break

  return list_of_coords

#function for computer ships
def computer_ship_locations():
  list_of_coords = []                 #create an empty list
  for ship in range(1,6):             #limits the drawing to 6 ships
    
    while True:
      x = random.randint(0,9)            #picks random intehger between 0 and 9
      y = random.randint(0,9)

      if (x,y) in list_of_coords:                 #test if the coordinate pair is not already taken
        print("This spot is already taken, please choose different x&y.")
      else:
        list_of_coords.append((x, y))               #all good - combine x&y and add to the list
        break

  return list_of_coords

#function to check if any of player's ships were hit
def player_ship_hit(player_coords, x, y):
  if (x, y) in player_coords:
    player_coords.remove((x, y))
    print("You have hit player's ship! The ship at x&y: ", x, y, "was destroyed.")
  else:
    print("Miss, better luck next time!")

#function to check if any of computer's ships were hit
def computer_ship_hit(computer_coords, x, y):
  if (x, y) in computer_coords:
    computer_coords.remove((x, y))    #if they were hit, remove from the list
    print("You have hit computer's ship! The ship at x&y: ", x, y, "was destroyed.")
  else:
    print("Miss, better luck next time!")

#function to play the game!
def game_play():
  #get the locations of the gueses
  player_coords = player_ship_locations()
  computer_coords = computer_ship_locations()

  #start the score keepig
  player_score = 0
  computer_score = 0

  #play the game
  while player_coords and computer_coords:

    #Ask player where to attack
    x = int(input("Enter the 'x' coordinate of your attack:"))
    y = int(input("Enter the 'y' coordinate of your attack:"))
    if (x,y) in computer_coords:
      computer_coords.remove((x, y))    #if they were hit, remove from the list
      player_score += 1                 #and add score
      print("Booom! You hit computer's ship at coordinates:", x, y, "and it was destroyed.")
    else:
      print("Miss, better luck next time!")
    print("Player's score:", player_score)  

    #Make computer attack
    #if computer_coords: 
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    if (x, y) in player_coords:
      player_coords.remove((x, y))      #if they were hit, remove from the list
      computer_score += 1               #and add score
      print("Boom! Computer hit your ship at coordinates:", x, y, "and it was destroyed.")  

    print("Computer's score:", computer_score)

# Check who's the winner
  if player_score > computer_score:
    print("Player wins with", player_score, "destroyed ships.")
  else:
    print("Computer wins with", computer_score, "destroyed ships.")


# Play the game
game_play()

#####################
#Future improvements that I didn't manage to do for now:
##game crashes if you press enter without writing antything - perhaps could fix it with raising the VlaueError exception?
##Adjust the game to be able to play with bigger ships (2x and 3x space)
###change the computer strategy from random to hitting next to the preivois hit (for 2x nad 3x ships)
####keep note of the x&y of the missed shot, so that you don't guess twice the same location