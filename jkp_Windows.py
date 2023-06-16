#!/usr/bin/python3

#------------------------------------------------------------
#IMPORTS
import random
import os

#------------------------------------------------------------
#VARIABLES
weapons_list = ["rock","paper","scissors"]
rude = ["Somebody's really bored.","That's not nice ...","Are you out of your cornfed mind?","Going somewhere?"]

USER_WINS = int(0)
COMP_WINS = int(0)
TIES      = int(0)

#------------------------------------------------------------
#FUNCTIONS DEFINITIONS

# for clearing the screen
def clearscreen():
    os.system("cls")

# let's being the game by asking for input
# weapons selection
def select_weapon():
    # lists (or arrays) start indexing at 0, so subtract 1 from the input
    i = (int(input("\n Select weapon: [1] ROCK [2] PAPER [3] SCISSORS [0] END: "))-1)     
    if i == -1:
        weapon = "end"
        return weapon
    
    elif i>2:
        weapon = "continue"
        return weapon
        
    else:
        weapon = weapons_list[i]        
        return weapon

# the actual game play
def play_game(weapon):
    global USER_WINS, COMP_WINS, TIES
    user_choice = weapon
    comp_choice = random.choice(weapons_list)    #randomize computer weapon selection
    
    if user_choice not in weapons_list:
        print(" Your weapon is not on the List!\n")
        return

    print(f" User: \t\t{user_choice.upper()}\n Computer: \t{comp_choice.upper()}\n")
    
    if user_choice == comp_choice:
        print(" It's a tie!")
        TIES += 1
    
    elif user_choice == "paper" and comp_choice == "rock":
        print(" You Win!")
        USER_WINS += 1
        
    elif user_choice == "rock" and comp_choice == "scissors":
        print(" You Win!")
        USER_WINS += 1
        
    elif user_choice == "scissors" and comp_choice == "paper":
        print(" You Win!")
        USER_WINS += 1
        
    else:
        print(" Computer Wins!")
        COMP_WINS += 1

# just a simple welcome screen / and then some advert for my youtube channel :)
clearscreen()
print(" A SIMPLE JAN-KEN-PON \n Please subscribe to my channel: youtube.com/MOTOJIN")


# looping, coz you might wanna play a few rounds (before you get bored...hehe)
while True:
    try:
        weapon = select_weapon()
        clearscreen()
        
        if weapon != "end":
            play_game(weapon)
        else:
            # Tally the final scores
            print(f" Total Win Scores:\t USER: {USER_WINS} | COMPUTER: {COMP_WINS} | TIES: {TIES}\n")
            
            # allow me a little advert for my youtube channel
            print(" Thanks for Playing ...")
            print(" Please subscribe to my channel: youtube.com/MOTOJIN")
            input()
            break
    except ValueError:
        # I'm lazy at handling errors, so ...
        clearscreen()
        msg = random.choice(rude)
        print(f" {msg}\n")
