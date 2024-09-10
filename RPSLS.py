import random

win_cons = {
    "scissors" : "paper",
    "paper" : "rock",
    "rock" : "lizard",
    "lizard" : "spock",
    "spock" : "scissors",
    "scissors" : "lizard",
    "lizard" : "paper",
    "paper" : "spock",
    "spock" : "rock",
    "rock" : "scissors"  
}

idx = 0
while(True):
    objects = ["rock", "paper", "scissors", "lizard", "spock"]
    player_choice = input("Choose rock, paper, lizard, spock or scissors, type q to quit \n")
    computer_choice = random.choice(objects)
    player_choice = player_choice.lower()

    if player_choice == computer_choice:
        print(f"The computer also chose {player_choice}")
    elif player_choice == 'q':
        break
    elif player_choice == win_cons[computer_choice]:
        print(f"computer chose {computer_choice}, you lose...")
    elif player_choice not in objects:
        print("The object you chose doesn't exist... Please check your spelling and try again")      
    else:
        print(f"computer chose {computer_choice}, you win!")

    if idx > 0:
        player_2_choice = prev_choice
        if player_2_choice == computer_choice:
            print(f"Player 2 and the computer both chose {player_2_choice}")
        elif player_2_choice == win_cons[computer_choice]:
            print(f"Player 2 chose {player_2_choice}... The computer beat player 2")
        elif player_choice not in objects:
            continue
        else:
            print(f"Player 2 chose {player_2_choice}, player 2 wins!") 

    idx = idx + 1
    prev_choice = player_choice
