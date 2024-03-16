import random

valid_inputs = ("rock", "paper", "scissors", "quit")
stats = {'wins': 0, 'losses': 0, 'draws': 0}
# winning combinations for the game
victories = [
    ["paper", "rock"],
    ["rock", "scissors"],
    ["scissors", "paper"]
    ]


def main():
    running = True
    while running:
        challenge = get_user_selection()
        guess = get_computer_selection()
        if challenge == "quit":
            print("OK, bye. Your final score was:")
            running = False
        else:
            determine_winner(challenge, guess)
        print(f"{stats['wins']} wins, and {stats['losses']} losses and {stats['draws']} draws,")


def get_user_selection():
    # prompt user to challenge computer to a valid game
    challenge = None
    while challenge not in valid_inputs:
        challenge = input("Choose rock, paper, scissors, or quit: ").lower()
    return challenge


def get_computer_selection():
    # generate random rock, paper, scissors
    guess = random.choice(valid_inputs[0:2])
    return guess


def determine_winner(challenge, guess):
    # determine winner and display result
    if challenge == guess:
        stats['draws'] += 1
        print("Draw! Try again")
    elif [challenge, guess] in victories:
        stats['wins'] += 1
        print(f"The {challenge} beats the {guess}, you win!")
    else:
        stats['losses'] += 1
        print(f"The {guess} beats the {challenge}, you lose!")


main()
