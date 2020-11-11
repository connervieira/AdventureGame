# Adventure Game - Conner Vieira
# Version: 1.0
# GPLv3 (https://www.gnu.org/licenses/gpl-3.0.txt)

# Configuration
# These variables can be modified to change how the game works

amount_of_tunnels = 5 # The amount of tunnels that players and dragons have to choose from. (Default: 5)
chance_of_escaping = 3 # How likely the player is to escape a dragon if they enter a tunnel with one. The higher the number, the less likely the player is to escape. Setting this to 1 means the character will escape every time. (Default: 3)
reveal_dragons = True # Determines whether or not the locations of all dragons will be revealed to the player after they lose. (Default: True)
debug_dragon_locations = False # Dumbs the dictionary containing the dragons and their locations at the beginning of every round. This is used for debugging, and shouldn't be set to True during normal games. (Default: False)

# End of configuration


import random # Needed to calculate random values, like the positions of dragons
import time # Needed to pause temporarily to allow the player to read on screen text
import os # Needed to clear the screen

class styles: # Define styles to apply to the console outputs later
  OK = '\033[92m' # Green
  WARNING = '\033[93m' # Yellow
  FAIL = '\033[91m' # Red
  BOLD = '\033[1m' # Bold
  UNDERLINE = '\033[4m' # Underline
  ENDC = '\033[0m' # Used to return to plain text after using a style


tunnelChoice = 0 # Placeholder variable for the tunnel selected by the player
while True: # Loop forever, only breaking when the player says they are done playing

  print("You are lost underground in a maze of tunnels with a dragon. Explore the tunnels without stumbling across any dragons!") # Print game introduction to the console
  time.sleep(4) # Wait 4 seconds before continuing

  dragonLocations = { # Dictionary to hold the positions of all dragons (dragon_number : dragon_location)
    1 : random.randint(1, amount_of_tunnels)
  }

  while True: # Loop forever, only breaking when the player loses
    if debug_dragon_locations == True:
      print(dragonLocations) # Dump the location of all dragons for debug purposes.

    tunnelChoice = int(input("Choose a tunnel, 1 through " + str(amount_of_tunnels) + ": ")) # Prompt the player for the tunnel they'd like to guess
    while tunnelChoice < 1 or tunnelChoice > amount_of_tunnels: # Repeat if the user doesn't choose an accepted number.
      tunnelChoice = int(input("Choose a tunnel, 1 through " + str(amount_of_tunnels) + ": ")) # Prompt the player for the tunnel they'd like to guess

    os.system('clear') # Clear the console
    print("You chose tunnel ", tunnelChoice) # Show the user their tunnel choice

    time.sleep(2) # Wait 2 seconds before continuing
    os.system('clear') # Clear the console

    if tunnelChoice in dragonLocations.values():
      print(f"{styles.FAIL}You entered a tunnel with a dragon!{styles.ENDC}") # Tell the player that they picked the wrong tunnel in red text

      time.sleep(2) # Wait 2 seconds before continuing

      print("You try to escape")

      time.sleep(2) # Wait 2 seconds before continuing

      if (random.randint(1, chance_of_escaping) == 1): # Give the player a chance of escaping the dragon and to continue playing
        print(f"{styles.OK}You successfully escaped the dragon!{styles.ENDC}") # Tell the player they successfully escaped the dragon
        input("Press enter once to continue") # Wait for the player to hit enter before continuing
      else:
        print(f"{styles.FAIL}You failed to escape the dragon!{styles.ENDC}") # Tell the player that they failed to escape the dragon
        input("Press enter once to continue") # Wait for the player to hit enter before continuing
        break # Exit the loop, since the player has lost
      
    else:
      print(f"{styles.OK}You entered an empty tunnel. You are safe for now.{styles.ENDC}") # Tell the player that they entered a safe tunnel in green text

      time.sleep(2) # Wait 2 seconds before continuing

      input("Press enter once to continue") # Wait for the player to hit enter before continuing
      
      os.system('clear') # Clear the console

      dragonLocations[len(dragonLocations) + 1] = random.randint(1, amount_of_tunnels) # Create a new dragon, place it in a random tunnel, and add it to the dictionary

      print(f"{styles.WARNING}Another dragon has entered the tunnels!{styles.ENDC}") # Warn the player that another dragon has entered the tunnels and has been placed somewhere randomly
      input("Press enter once to continue") # Wait for the player to hit enter before continuing

  os.system('clear') # Clear the console
  print(f"{styles.BOLD}GAME OVER{styles.ENDC}") # Print Game Over message to console
  if reveal_dragons == True:
    for key, value in dragonLocations.items():
      print("Dragon " + str(key) + " was in tunnel " + str(value))
    print("") # Create line break at the end of the list of dragon locations

  if (input("Would you like to play again? (y/n): ") == "n"):
    break
  os.system('clear') # Clear the console
  
os.system('clear') # Clear the console
print("Bye!")
