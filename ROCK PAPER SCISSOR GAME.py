#Made My Rupankar Garai


import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock":
        return "Player wins!" if computer_choice == "scissors" else "Computer wins!"
    elif player_choice == "paper":
        return "Player wins!" if computer_choice == "rock" else "Computer wins!"
    elif player_choice == "scissors":
        return "Player wins!" if computer_choice == "paper" else "Computer wins!"
    else:
        return "Invalid choice. Please choose rock, paper, or scissors."

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock-Paper-Scissors!")
    play_again = "yes"

    while play_again.lower() == "yes":
        computer_choice = random.choice(choices)
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice in choices:
            print("Computer chose:", computer_choice)
            result = determine_winner(player_choice, computer_choice)
            print(result)
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

        play_again = input("Do you want to play again? (yes/no): ")

    print("Thank you for playing!")

rock_paper_scissors()


#end of the code