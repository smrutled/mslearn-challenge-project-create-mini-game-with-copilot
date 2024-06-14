# create a console game that is based on rock, paper, scissors. 
# The game should be able to take in user input and randomly select a computer choice.
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def game():
    player_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options)
        if player_choice not in options:
            print("Invalid option. Please enter rock, paper, or scissors.")
            continue
        print(f"Computer chose {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player_choice == "scissors":
            if computer_choice == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        print(f"Player: {player_score} Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"Final score: Player: {player_score} Computer: {computer_score}")

if __name__ == "__main__":
    game()
    