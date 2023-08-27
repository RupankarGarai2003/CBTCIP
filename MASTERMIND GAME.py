#Made By Rupankar Garai

#first import random to generate 4 digit secret code randomly

import random

def generate_secret_code():
    return str(random.randint(1000, 9999))  # Generate a 4-digit secret code

def get_hint(secret_code, guess):
    hint = []
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            hint.append(guess[i])
        else:
            hint.append("*")
    return "".join(hint)

def player2_turn(secret_code):
    attempts = 0
    while True:
        guess = input("Player 2's Guess: ")
        attempts += 1
        if guess == secret_code:
            print("Player 2 wins! Code:", secret_code)
            break
        else:
            hint = get_hint(secret_code, guess)
            print("Hint:", hint)

    return attempts

def player1_turn():
    return input("Player 1, Please Enter Your Secret Code: ")

def player_vs_player_game():
    player1_code = player1_turn()
    player2_attempts = player2_turn(player1_code)
    
    player2_code = generate_secret_code()
    print("Player 1's Turn To Guess Player 2's Code!")
    player1_attempts = player2_turn(player2_code)

    if player1_attempts < player2_attempts:
        print("Player 1 Wins! Took Fewer Attempts.")
    elif player2_attempts < player1_attempts:
        print("Player 2 wins! Took Fewer Attempts.")
    else:
        print("It's a Tie!")

player_vs_player_game()


#end of the code